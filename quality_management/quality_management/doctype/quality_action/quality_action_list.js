frappe.listview_settings['Quality Action'] = {
	add_fields: ["status"],
	add_fields: ["action"],
	get_indicator: function(doc) {
		if(doc.status == "Planned") {
			return [__("Planned"), "yellow", "status,=,Planned"];
		}
		else if(doc.status == "Under Review") {
			return [__("Under Review"), "green", "status,=,Under Review"];
		}
		else if(doc.status == "Patched") {
			return [__("Patched"), "blue", "status,=,Patched"];	
		}
	}	
}
