# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class CustomerFeedback(Document):
	
	def before_insert(self):
		for data in self.feedback:
			print(data.rating)

	def after_insert(self):
		query = frappe.get_list("Quality Action", filters={"feedback": ""+ self.name +""})
		if len(query) == 0:
			doc = frappe.get_doc({
				'doctype': 'Quality Action',
				'action': 'Corrective',
				'type': 'Customer Feedback',
				'feedback': ''+ self.name +'',
				'date': ''+ frappe.utils.nowdate() +''
			})
			for data in self.feedback:
				print(data.qualitative_feedback)
				doc.append("description",{
					'problem': data.qualitative_feedback,
					'status': 'Opened'
				})
			doc.insert()
			frappe.db.commit()