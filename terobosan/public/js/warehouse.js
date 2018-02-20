frappe.ui.form.on("Warehouse", {
	refresh: function(frm) {
    //cur_frm.toggle_display("Stock Balance", doc.__islocal ? 1 : 0);

    //frm.toggle_display(['address_html','contact_html'], !frm.doc.__islocal);
    //if (frm.custom_buttons) frm.clear_custom_buttons();
    //frm.events.add_context_buttons(frm);

    cur_frm.clear_custom_buttons();


    frm.add_custom_button(__("<button class='btn btn-success btn-xs btn-custom'>Stock Balance1</button>"), function() {
			frappe.set_route("query-report", "Stock Balance", {"warehouse": frm.doc.name});


		});
		frm.add_custom_button(__("<button class='btn btn-danger btn-xs btn-custom'>Stock Balance1</button>"), function() {
			frappe.set_route("query-report", "Stock Balance", {"warehouse": frm.doc.name});


		});

		//cur_frm.toggle_display("Stock Balance", show);

    frm.add_custom_button(__("<button class='btn btn-warning btn-xs'>Get User Email Address</button>"), function(){
        frappe.set_route("query-report", "Stock Balance", {"warehouse": frm.doc.name});
    }, __("Utilities"));

    frm.add_custom_button(__('Get User Email Address1'), function(){
        frappe.set_route("query-report", "Stock Ledger", {"warehouse": frm.doc.name});
    }, __("Utilities"));

	}
});

cur_frm.cscript.refresh = function(doc) {

	cur_frm.set_intro(doc.__islocal ? "" : __("There is nothing to edit."))
	cur_frm.set_intro(__('Default theme is set in {0}', ['<a href="#Form/Website Settings">'
+ __('Website Settings') + '</a>']));

}
