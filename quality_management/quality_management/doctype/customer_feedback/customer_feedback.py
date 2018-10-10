# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class CustomerFeedback(Document):
	
	def after_insert(self):
		print(self.name)
		doc = frappe.get_doc({
			'doctype': 'Quality Action',
			'action': 'Corrective',
			'type': 'Customer Feedback',
			'feedback': ''+ self.name +'',
			'date': ''+ frappe.utils.nowdate() +'',
			'problem': ''+ self.description +''
		})
		doc.insert()
		doc.name