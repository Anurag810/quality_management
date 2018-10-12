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
		var n = a.indexOf("Daily");
		if (n != -1){
			 frm.set_value("next_date", frappe.datetime.add_days(frappe.datetime.get_today(), 1));
}
	}
});

