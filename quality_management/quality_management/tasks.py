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
	day = now.day
	day_name = now.strftime("%A")
	month=now.strftime("%B")

	for data in frappe.get_all("Quality Goal",fields=['name','scheduler','frequency']):
		print("----"+data.name)
		print("--------"+data.scheduler)
		print("--------"+data.frequency)
		if data.frequency.find("Everyday") > -1:
			pass
		elif data.frequency.find("Weekly") > -1:
			if data.scheduler == day_name:
				pass
		elif data.frequency.find("Monthly") > -1:
			if data.scheduler == str(day):
				pass
		elif data.frequency.find("Quarterly") > -1:
			if month == 'January' and day == 1:
				pass
			elif month == 'April' and day == 1:
				pass
			elif month == 'July' and day == 1:
				pass
			elif month == 'October' and day == 1:
				pass
		elif data.frequency.find("Half") > -1:
			if month == 'January' and day == 1:
				pass
			elif month == 'July' and day == 1:
				pass
		elif data.frequency.find("Yearly") > -1:
			if month == 'January' and day == 1:
				pass

#	data = frappe.get_doc('Quality Goal')
#	goals = [frappe.get_doc('Quality Goal', d.name) for d in data]
#	objectives = [[d.objective for d in goal.objective] for goal in goals]
#	targets = [[d.target for d in goal.objective] for goal in goals]
#	units = [[d.unit for d in goal.objective] for goal in goals]

#	doc = frappe.get_doc({
#		'doctype': 'Quality Review',
#	})
#	doc.insert()
#	doc.name