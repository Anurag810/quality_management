// Copyright (c) 2018, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Quality Monitoring Frequency', {
	refresh: function(frm) {

	},
	frequency: function(frm){
		var frequency = frm.get_field("frequency").value;
		if (frequency == "Daily"){
			frm.set_df_property("day", "options", "A\nB\nC");
		}
		else if (frequency == "Weekly"){
			frm.set_df_property("day", "options", "A\nB\nC");
		}
		else if (frequency == "Monthly"){

		}
		else if (frequency == "Quarterly"){

		}
		else if (frequency == "Half-Yearly"){

		}
		else{

		}
	}
});
