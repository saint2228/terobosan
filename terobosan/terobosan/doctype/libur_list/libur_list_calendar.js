// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

frappe.views.calendar["Libur List"] = {
	field_map: {
		"start": "libur_date",
		"end": "libur_date",
		"id": "name",
		"title": "description",
		"allDay": "allDay"
	},
	get_events_method: "terobosan.terobosan.doctype.libur_list.libur_list.get_events",
	filters: [
		{
			'fieldtype': 'Link',
			'fieldname': 'libur_list',
			'options': 'Libur List',
			'label': __('Libur List')
		}
	]
}
