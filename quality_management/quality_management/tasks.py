from __future__ import unicode_literals
import frappe
from frappe.utils import date_diff, nowdate, formatdate, add_days

def audit():
	doc = frappe.get_doc({
		'doctype': 'Quality Audit',
		'from_date': ''+ frappe.utils.nowdate() +'',
        'status':'Scheduled',
        'action':'Under Review'
	})
	doc.insert()
	doc.name

def review():
    	doc = frappe.get_doc({
		'doctype': 'Quality Review',
		
	})
	doc.insert()
	doc.name