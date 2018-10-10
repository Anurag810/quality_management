# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class QualityAudit(Document):
	def after_insert(self):
		action = ''
		if self.status == "Non Conformance":
			query = frappe.db.sql(""" SELECT * from `tabQuality Action` WHERE audit='"""+self.name+"""'""", as_dict=1)
			if len(query) == 0:
				action += "IN "+self.name+" due to non-conformation in Procedure "+self.procedure+" by :- "+self.auditor

				if(action != ''):
					doc = frappe.get_doc({
					'doctype': 'Quality Action',
					'action': 'Preventive',
					'type': 'Quality Audit',
					'audit': ''+ self.name +'',
					'date': ''+ frappe.utils.nowdate() +'',
					'problem': ''+ action +''
					})
					doc.insert()
					doc.name

	def on_update(self):
		print("Running on Update method")
		if self.status == "Non Conformance":
			action = ''
			query = frappe.db.sql(""" SELECT * from `tabQuality Action` WHERE audit='"""+self.name+"""'""", as_dict=1)
			if len(query) !=0:
				action += "IN "+self.name+" due to non-conformation in Procedure "+self.procedure+" by :-* "+self.auditor
				query = frappe.db.sql("""UPDATE `tabQuality Action` SET problem='"""+ action +"""' WHERE audit='"""+self.name+"""'""")
		else:
			query = frappe.db.sql("""DELETE from `tabQuality Action` WHERE audit='"""+self.name+"""'""")




		


