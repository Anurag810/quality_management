// Copyright (c) 2018, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Quality Goal', {
	refresh: function(frm) {

	},
	revision: function(frm) {
		frm.set_value("revised_on", frappe.datetime.get_today())
	},
	scope: function(frm) {
		//	frm.set_value("revised_on", get_today())
	}
});

frappe.ui.form.on('Quality Objective', {
	frequency(frm, cdt, cdn) {
		console.log(frm.fields_dict)
		objective = frappe.get_doc(cdt, cdn)
		// console.log(objective)
		// if objective.frequency == "Weekly":
		// 	objective.
		// if objective.frequency == "Weekly":
		// objective.
	}
});
