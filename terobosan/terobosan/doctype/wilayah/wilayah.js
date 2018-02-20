// Copyright (c) 2018, ridhosribumi and contributors
// For license information, please see license.txt

cur_frm.cscript.refresh = function(doc,cdt,cdn) {
	cur_frm.cscript.set_root_readonly(doc);
}

cur_frm.cscript.set_root_readonly = function(doc){
	if(!doc.parent_wilayah){
		cur_frm.set_read_only();
		cur_frm.set_intro(__("This is a root wilayah and cannot be edited."));
	} else {
		cur_frm.set_intro(null);
	}
}

cur_frm.fields_dict['parent_wilayah'].get_query = function(doc,cdt,cdn){
	return{
		filters:[
			['Wilayah','is_group','=', 1],
			['Wilayah','name','!=',doc.wilayah_name]
		]
	}
}
