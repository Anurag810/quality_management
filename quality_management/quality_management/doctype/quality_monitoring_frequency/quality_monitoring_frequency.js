// Copyright (c) 2018, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Quality Monitoring Frequency', {
	onload: function(frm) {
		frm.set_df_property("day", "options", "Everyday");
	},
	frequency: function(frm){
		var frequency = frm.get_field("frequency").value;
		if (frequency == "Daily"){
			frm.set_df_property("day", "options", "Everyday");
		}
		else if (frequency == "Weekly"){
			frm.set_df_property("day", "options", "Monday\nTuesday\nWednesday\nThursday\nFriday\nSaturday");
		}
		else if (frequency == "Monthly"){
			frm.set_df_property("day", "options", "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n16\n17\n18\n19\n20\n21\n22\n23\n24\n25\n26\n27\n28");
		}
		else if (frequency == "Quarterly"){
			frm.set_df_property("day", "options", "January 1-April 1-July 1-October 1");
		}
		else if (frequency == "Half Yearly"){
			frm.set_df_property("day", "options", "January 1-July 1");
		}
		else{
			frm.set_df_property("day", "options", "January 1");
		}
	}
});
