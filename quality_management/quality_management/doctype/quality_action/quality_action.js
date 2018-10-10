// Copyright (c) 2018, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Quality Action', {
	refresh: function(frm) {

	},
	onload: function(frm) {
		frm.set_value("date", frappe.datetime.get_today())
	},
	review: function(frm){
		frappe.call({
            "method": "frappe.client.get",
            args: {
                doctype: "Quality Review",
				name: frm.doc.review
            },
            callback: function (data) {
				var review = "";
				for (var i = 0; i < data.message.values.length; i++ ){
					if (data.message.values[i].achieved < data.message.values[i].target){
						review = review + "For " + data.message.values[i].objective + ", Achieved Value : " + data.message.values[i].achieved + " is Less than Target Value " + data.message.values[i].target + "\n"; 
					}
				}
				frm.set_value("problem", review);
            }
        })
	},
	audit: function(frm){

	},
	feedback: function(frm) {
		frappe.call({
			"method": "frappe.client.get",
			args: {
				doctype: "Customer Feedback",
				name: frm.doc.feedback
			},
			callback: function(data){
				frm.set_value("problem", data.message.description)
			}
		})
	}
});
