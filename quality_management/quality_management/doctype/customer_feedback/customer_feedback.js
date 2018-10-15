// Copyright (c) 2018, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Customer Feedback', {
	refresh: function(frm) {

	},
	onload: function(frm){
		frm.set_value("date", frappe.datetime.get_today())
	},
	customer: function(frm){
		
	},
	template: function(frm){
		frappe.call({
            "method": "frappe.client.get",
            args: {
                doctype: "Feedback Template",
				name: frm.doc.template
            },
            callback: function (data) {
				console.log(data.message);
				for (var i = 0; i < data.message.feedback_parameter.length; i++ ){
					frm.add_child("feedback");
					frm.fields_dict.feedback.get_value()[i].parameter = data.message.feedback_parameter[i].parameter;
				}
				frm.refresh();
            }
        })
	}
});
