frappe.listview_settings['Feedback Template'] = {
	add_fields: ["scope"],
	get_indicator: function(doc) {
		if(doc.scope == "Company") {
			return [__("Conpany"), "red", "status,=,Company"];
		}
		else if(doc.scope == "Department") {
			return [__("Department"), "green", ",status,=,Department"];
		}		
	}	
}