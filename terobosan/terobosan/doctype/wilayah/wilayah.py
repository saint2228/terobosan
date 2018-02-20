# -*- coding: utf-8 -*-
# Copyright (c) 2018, ridhosribumi and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

from frappe.utils import flt
from frappe import _

#from frappe.model.document import Document
from frappe.utils.nestedset import NestedSet

class Wilayah(NestedSet):
	nsm_parent_field = 'parent_wilayah'

	def on_update(self):
		super(Wilayah,self).on_update()
		self.validate_one_root()
