// Copyright (c) 2018, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Quality Action', {
	refresh: function(frm) {

	},
	onload: function(frm) {
		frm.set_value("date", frappe.datetime.get_today())
		if (frm.doc.review != null){
			frm.set_value("type", "Quality Review")
		}
		else if(frm.doc.feedback != null){
			frm.set_value("type", "Customer Feedback")
		}
		else{
			frm.set_value("type", "Quality Review")
		}
	},
	review: function(frm){
		var problems = "";
		if (frm.doc.review != null){
			frm.fields_dict.description.grid.remove_all()
			frm.refresh();
		}
		frappe.call({
            "method": "frappe.client.get",
            args: {
                doctype: "Quality Review",
				name: frm.doc.review
            },
            callback: function (data) {
				for (var i = 0; i < data.message.values.length; i++ ){
					if (data.message.values[i].achieved < data.message.values[i].target){
						problems += data.message.values[i].objective +"-"+ data.message.values[i].achieved + " " + data.message.values[i].target_unit + "\n";
					}
				}
				problems= problems.replace(/\n$/, "").split("\n");
				for (var i = 0; i < problems.length; i++){
					frm.add_child("description");
					frm.fields_dict.description.get_value()[i].problem = problems[i];
				}
				//frm.refresh();
            }
		})
		frappe.call({
            "method": "frappe.client.get",
            args: {
                doctype: "Quality Goal",
				name: frm.doc.goal
            },
            callback: function (data) {
				console.log(data.message.procedure);
				frm.doc.procedure = data.message.procedure;
				frm.refresh();
            }
        })
	},
	feedback: function(frm) {
		if (frm.doc.feedback != null){
			frm.fields_dict.description.grid.remove_all()
			frm.refresh();
		}
		frm.doc.description = [];
		frm.refresh();
		frappe.call({
			"method": "frappe.client.get",
			args: {
				doctype: "Customer Feedback",
				name: frm.doc.feedback
			},
			callback: function(data){
				for (var i = 0; i < data.message.feedback.length; i++ ){
					frm.add_child("description");
					frm.fields_dict.description.get_value()[i].problem = data.message.feedback[i].parameter +"-"+ data.message.feedback[i].qualitative_feedback;
				}
				frm.refresh();
			}
		})
	},
	type: function(frm){
		if(frm.doc.description != null){
			frm.fields_dict.description.grid.remove_all()
			frm.doc.review = '';
			frm.doc.feedback = '';
			frm.doc.goal = '';
			frm.doc.procedure = '';
			frm.refresh();
		}
	}
});
