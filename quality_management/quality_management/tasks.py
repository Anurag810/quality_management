from __future__ import unicode_literals
import frappe
from frappe.utils import date_diff, nowdate, formatdate, add_days

#def all():
#	doc = frappe.get_doc({
#		'doctype': 'Quality Action',
#		'action': 'Corrective',
#		'type': 'Quality Review',
#		'date': ''+ frappe.utils.nowdate() +'',
#		'problem': 'hello'
#	})
#	doc.insert()
#	doc.name