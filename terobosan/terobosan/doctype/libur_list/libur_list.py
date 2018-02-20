# -*- coding: utf-8 -*-
# Copyright (c) 2018, ridhosribumi and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import json
from frappe.utils import getdate,cint, formatdate
from frappe import throw, _
from frappe.model.document import Document

class LiburList(Document):
	def validate(self):
		self.validate_days()

	def clear_table(self):
		self.set('libur',[])

	def validate_values(self):
		if not self.weekly_off:
			throw(_("Please select weekly off day"))

	def validate_days(self):
		if self.from_date > self.to_date:
			throw(_("To Date cannot be before From Date"))

		for day in self.get("libur"):
			if not (getdate(self.from_date) <= getdate(day.libur_date) <= getdate(self.to_date)):
				frappe.throw(_("The libur on {0} is not between From Date and To Date").format(formatdate(day.libur_date)))

	def get_weekly_off_dates(self):
		self.validate_values()
		date_list = self.get_weekly_off_date_list(self.from_date, self.to_date)
		last_idx = max([cint(d.idx) for d in self.get("libur")] or [0,])
		for i, d in enumerate(date_list):
			ch = self.append('libur', {})
			ch.description = self.weekly_off
			ch.libur_date = d
			ch.idx = last_idx + i + 1

	def get_weekly_off_date_list(self, start_date, end_date):
		start_date, end_date = getdate(start_date), getdate(end_date)

		from dateutil import relativedelta
		from datetime import timedelta
		import calendar

		date_list = []
		existing_date_list = []
		weekday = getattr(calendar, (self.weekly_off).upper())
		reference_date = start_date + relativedelta.relativedelta(weekday=weekday)

		existing_date_list = [getdate(libur.libur_date) for libur in self.get("libur")]

		while reference_date <= end_date:
			if reference_date not in existing_date_list:
				date_list.append(reference_date)
			reference_date += timedelta(days=7)

		return date_list

@frappe.whitelist()
def get_events(start, end, filters=None):
	"""Returns events for Gantt / Calendar view rendering.

	:param start: Start date-time.
	:param end: End date-time.
	:param filters: Filters (JSON).
	"""
	if filters:
		filters = json.loads(filters)
	else:
		filters = []

	if start:
		filters.append(['Libur', 'libur_date', '>', getdate(start)])
	if end:
		filters.append(['Libur', 'libur_date', '<', getdate(end)])

	return frappe.get_list('Libur List',
		fields=['name', '`tabLibur`.libur_date', '`tabLibur`.description'],
		filters = filters,
		update={"allDay": 1})
