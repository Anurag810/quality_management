// Copyright (c) 2018, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Quality Goal', {
	refresh: function(frm) {

	},
	revision: function(frm) {
		frm.set_value("revised_on", frappe.datetime.get_today())
	},
	frequency: function(frm){
		var a = frm.doc.frequency;
		if (a.indexOf("Daily") != -1){
			 frm.set_value("next_date", frappe.datetime.add_days(frappe.datetime.get_today(), 1));
		}
		else if(a.indexOf("Weekly") != -1){
			alert("Weekly");
		}
		else if(a.indexOf("Monthly") != -1){
			alert("Monthly");
		}
		else if(a.indexOf("Quarterly") != -1){
			alert("Q")
		}
		else if(a.indexOf("Half") != -1){
			alert("Half");
		}
		else if(a.indexOf("Yearly") != -1){
			alert("Yearly");
		}

	}
});

