frappe.listview_settings['Quality Meeting'] = {
	add_fields: ["status"],
	get_indicator: function(doc) {
		if(doc.status == "Open") {
			return [__("Open"), "red", "status=,Open"];
		}
		else if(doc.status == "Closed") {
			return [__("Close"), "green", ",status=,Close"];
		}		
	}	
}