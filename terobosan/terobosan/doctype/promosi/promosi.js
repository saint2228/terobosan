// Copyright (c) 2018, ridhosribumi and contributors
// For license information, please see license.txt

frappe.ui.form.on("Promosi", "refresh", function(frm) {

		erpnext.toggle_naming_series();
		if(frm.doc.__islocal) {
			frm.toggle_display("naming_series", frappe.boot.sysdefaults.campaign_naming_by=="Naming Series");
		}
		else{
			cur_frm.add_custom_button(__("View Leads"), function() {
				frappe.route_options = {"source": "Promosi","promosi_name": frm.doc.name}
				frappe.set_route("List", "Lead");
			}, "fa fa-list", true);
	}
})
