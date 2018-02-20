# -*- coding: utf-8 -*-
# Copyright (c) 2018, ridhosribumi and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname

class Promosi(Document):
	def autoname(self):
		if frappe.defaults.get_global_default('campaign_naming_by') != 'Naming Series':
			self.name = self.promosi_name
		else:
			self.name = make_autoname(self.naming_series+'.#####')
