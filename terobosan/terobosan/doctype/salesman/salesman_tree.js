frappe.treeview_settings["Salesman"] = {
  fields: [
    {fieldtype:'Data',fieldname: 'salesman_name',
      label:__('New Salesman Name'),reqd:true},
    {fieldtype:'Link',fieldname: 'employee',
      label:__('Employee'),options:'Employee',
      description: __("Please enter Employee Id of this salesman")},
    {fieldtype:'Check',fieldname: 'is_group', label:__('Group Node'),
      description: __("Further nodes can be only created under 'Group' type nodes")}
  ],
}
