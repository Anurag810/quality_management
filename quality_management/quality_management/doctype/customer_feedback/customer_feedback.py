# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class CustomerFeedback(Document):
	
	def validate(self):
		rating = 0
		total = 5 * len(self.feedback)
		for data in self.feedback:
			rating += int(data.rating)

		if (rating*100)/total < 75:
			self.action = "Action Initialised"
		

	def after_insert(self):
		rating = 0
		total = 5 * len(self.feedback)
		for data in self.feedback:
			rating += int(data.rating)

		if (rating*100)/total < 75:
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
		else:
			pass