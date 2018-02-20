# -*- coding: utf-8 -*-
# Copyright (c) 2018, ridhosribumi and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils.nestedset import NestedSet

class Salesman(NestedSet):
	nsm_parent_field = 'parent_salesman';

	def validate(self):
		self.validate_employee_id()

	def on_update(self):
		super(Salesman, self).on_update()
		self.validate_one_root()

	def validate_employee_id(self):
		salesman = frappe.db.get_value("Salesman", {"employee": self.employee})

		if salesman and salesman !=self.name:
			frappe.throw(_("Another Salesman {0} exists with same Employee id").format(salesman))
