// Copyright (c) 2018, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Customer Survey', {
	refresh: function(frm) {

	},
	customer: function(frm){
		frm.set_value("date", frappe.datetime.get_today())
	}
});
