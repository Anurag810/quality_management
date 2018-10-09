// Copyright (c) 2018, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Quality Review', {
	refresh: function(frm) {

	},
	goal: function(frm) {
		frm.set_value("date", frappe.datetime.get_today())
		frappe.call({
            "method": "frappe.client.get",
            args: {
                doctype: "Quality Goal",
				name: frm.doc.goal
            },
            callback: function (data) {
				//console.log(data.message.objective[0]);
				for (var i = 0; i < data.message.objective.length; i++ ){
					//if(i != 0){
						frm.add_child("values");
					//}
					frm.fields_dict.values.get_value()[i].objective = data.message.objective[i].objective;
					frm.fields_dict.values.get_value()[i].target = data.message.objective[i].target;
					frm.fields_dict.values.get_value()[i].target_unit = data.message.objective[i].unit;
					frm.fields_dict.values.get_value()[i].achieved_unit = data.message.objective[i].unit;
				}
				frm.refresh();
            }
        })
	},
});