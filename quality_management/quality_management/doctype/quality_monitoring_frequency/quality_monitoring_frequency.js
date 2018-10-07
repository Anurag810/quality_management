// Copyright (c) 2018, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Quality Monitoring Frequency', {
	refresh: function(frm) {

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
			frm.set_df_property("day", "options", "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n16\n17\n18\n19\n20\n21\n22\n23\n24\n25\n26\n27\n28\n29\n30\n31");
		}
		else if (frequency == "Quarterly"){
			frm.set_df_property("day", "options", "First Quarter-January 1\nSecond Quarter-April 1\nThird Quarter-July 1\nFourth Quarter-October 1");
		}
		else if (frequency == "Half Yearly"){
			frm.set_df_property("day", "options", "First Half-January 1\nSecond Half-July 1");
		}
		else{
			frm.set_df_property("day", "options", "Year-January 1");
		}
	}
});
