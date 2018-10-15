// Copyright (c) 2018, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Quality Goal', {
	refresh: function(frm) {

	},
	revision: function(frm) {
		frm.set_value("revised_on", frappe.datetime.get_today())
	},
	weekly: function(frm) {
		if(frm.doc.frequency == "Weekly"){
          frm.set_value("scheduler",frm.doc.weekly)
		}},
	monthly: function(frm){
		if(frm.doc.frequency == "Monthly"){
			frm.set_value("scheduler",frm.doc.monthly)
	}
	},
	onload,frequency: function(frm){
		if(frm.doc.frequency == "Weekly"){frm.set_value("scheduler","Monday")}
		if(frm.doc.frequency == "Monthly"){frm.set_value("scheduler","1")}

	},

	
	
});

