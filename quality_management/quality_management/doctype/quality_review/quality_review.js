// Copyright (c) 2018, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Quality Review', {
	refresh: function(frm) {

	},
	procedure: function(frm) {
		frm.set_value("date", frappe.datetime.get_today())
		frappe.call({
            "method": "frappe.client.get",
            args: {
                doctype: "Quality Goal",
				name: frm.doc.goal
            },
            callback: function (data) {
				var string = "";
				for (var i = 0; i < data.message.objective.length; i++ ){
					string = string + data.message.objective[i].objective;
					if (i != data.message.objective.length-1 ){
						string = string + "\n";	
					}
				}
				frm.set_df_property("objective", "options", string)
            }
        })
	},
	objective: function(frm) { 
		frappe.call({
            "method": "frappe.client.get",
            args: {
                doctype: "Quality Goal",
				name: frm.doc.goal
            },
            callback: function (data) {
				for (var i = 0; i < data.message.objective.length; i++ ){
					if (data.message.objective[i].objective == frm.doc.objective){
						frm.set_value("target", data.message.objective[i].target);
					}
				}
			}
        })
	}
});