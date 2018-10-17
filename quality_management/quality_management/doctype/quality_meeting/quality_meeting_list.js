frappe.listview_settings['Customer Meeting'] = {
	add_fields: ["status"],
	get_indicator: function(doc) {
		if(doc.status == "Opened") {
			return [__("Opened"), "green", "status=,Opened"];
		}
		else if(doc.status == "Closed") {
			return [__("Closed"), "red", ",status=,Closed"];
		}		
	}	
}