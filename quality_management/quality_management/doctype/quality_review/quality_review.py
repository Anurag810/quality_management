# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class QualityReview(Document):
	
	def after_insert(self):
		problem = ''
		print("""SELECT * FROM `tabQuality Review` WHERE review='"""+self.name+"""'""")
		query = frappe.db.sql("""SELECT * FROM `tabQuality Action` WHERE review='"""+self.name+"""'""", as_dict=1)
		print(len(query))
		if len(query) == 0:
			for value in self.values:
				if value.achieved < value.target:
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
	def on_update(self):
		problem = ''		
		for value in self.values:
			if value.achieved < value.target:
				problem = problem + 'In '+ value.objective +', the Achieved Value '+ str(value.achieved) +' is less than the Target Value '+ str(value.target) +'\n'
			
		if problem != '':
			print(""""UPDATE `tabQuality Action` SET review='"""+ problem +"""' WHERE review='"""+self.name+"""'""")
			query = frappe.db.sql("""UPDATE `tabQuality Action` SET problem='"""+ problem +"""' WHERE review='"""+self.name+"""'""")
		else:
			query = frappe.db.sql("""DELETE FROM `tabQuality Action` WHERE review='"""+self.name+"""'""")

