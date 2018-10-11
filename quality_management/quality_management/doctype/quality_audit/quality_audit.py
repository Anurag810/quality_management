# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class QualityAudit(Document):

	def on_update(self):
		if frappe.utils.nowdate() == self.to_date:
			query = frappe.db.sql("""SELECT * FROM `tabQuality Action` WHERE audit='"""+self.name+"""'""", as_dict=1)

			if len(query) == 0:
				print("Original")
				if self.status == "Non Conformance":		
					doc = frappe.get_doc({
						'doctype': 'Quality Action',
						'action': 'Corrective',
						'type': 'Quality Audit',
						'audit': ''+ self.name +'',
						'date': ''+ frappe.utils.nowdate() +'',
						'problem': 'Non-Conformance in Audit '+ self.name +''
					})
					doc.insert()
					doc.name
			else:
				print("Duplicate")
				if self.status == "Non Conformance":
					query = frappe.db.sql("""UPDATE `tabQuality Action` SET problem='Non-Conformance in Audit """+ self.name +"""' WHERE audit='"""+self.name+"""'""")
				else:
					query = frappe.db.sql("""DELETE FROM `tabQuality Action` WHERE audit='"""+self.name+"""'""")
		else:
			pass
