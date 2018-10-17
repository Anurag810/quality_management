frappe.listview_settings['Quality Review'] = {
	add_fields: ["scope"],
	get_indicator: function(doc) {
		if(doc.scope == "Company") {
			return [__("Company"), "blue", "scope,=,Company"];
		}
		else if(doc.scope == "Department") {
			return [__("Department"), "green", "scope,=,Department"];
		}		
	}	
}