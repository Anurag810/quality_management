from __future__ import unicode_literals
import frappe
import datetime
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
	data = frappe.get_doc('Quality Goal')
	goals = [frappe.get_doc('Quality Goal', d.name) for d in data]
	objectives = [[d.objective for d in goal.objective] for goal in goals]
	targets = [[d.target for d in goal.objective] for goal in goals]
	units = [[d.unit for d in goal.objective] for goal in goals]