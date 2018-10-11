# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class QualityReview(Document):
	
	def on_update(self):
		problem = ''
		query = frappe.db.sql("""SELECT * FROM `tabQuality Action` WHERE review='"""+self.name+"""'""", as_dict=1)

		if len(query) == 0:
			for value in self.values:
				if int(value.achieved) < int(value.target):
					problem = problem + 'In '+ value.objective +', the Achieved Value '+ str(value.achieved) +' is less than the Target Value '+ str(value.target) +'\n'
			
			if(problem != ''):		
				doc = frappe.get_doc({
					'doctype': 'Quality Action',
					'action': 'Corrective',
					'type': 'Quality Review',
					'review': ''+ self.name +'',
					'date': ''+ frappe.utils.nowdate() +'',
					'problem': ''+ problem +''
				})
				doc.insert()
				doc.name
		else:
			for value in self.values:
				if int(value.achieved) < int(value.target):
					problem = problem + 'In '+ value.objective +', the Achieved Value '+ str(value.achieved) +' is less than the Target Value '+ str(value.target) +'\n'

			if problem != '':
				query = frappe.db.sql("""UPDATE `tabQuality Action` SET problem='"""+ problem +"""' WHERE review='"""+self.name+"""'""")
			else:
				query = frappe.db.sql("""DELETE FROM `tabQuality Action` WHERE review='"""+self.name+"""'""")
