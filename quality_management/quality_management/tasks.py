from __future__ import unicode_literals
import frappe
from frappe.utils import date_diff, nowdate, formatdate, add_days

def create_audit():
	doc = frappe.get_doc({
		'doctype': 'Quality Audit',
		'from_date': ''+ frappe.utils.nowdate() +'',
        'status':'Scheduled',
        'action':'Under Review'
	})
	doc.insert()
	doc.name