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
	now = datetime.datetime.now()
	date = now.day
	day_name = now.strftime("%A")
	for data in frappe.get_all("Quality Goal",fields=['name','scheduler','scope']):
		print(data.scheduler)
		if data.scheduler == "Everyday":
			print("-----------------------------------------------------------------------------------Everyday")
		if data.scheduler == day_name:
			print("---------------------------------------------------------------------------weekly-"+day_name)
		if data.scheduler == str(date):
			print("---------------------------------------------------------------------------Monthly-" + str(date))