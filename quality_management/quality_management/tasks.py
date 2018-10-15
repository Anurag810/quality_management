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

	def get_objective(name):
		objectives = frappe.get_all("Quality Objective", filters={'parent': ''+ name +''}, fields=['objective', 'target', 'unit'])
		return objectives

	for data in frappe.get_all("Quality Goal",fields=['name','scheduler','frequency']):
		if data.frequency.find("Everyday") > -1:
			print("EVERYDAY----"+ data.name)
			objectives = get_objective(data.name)
			print(objectives)

		elif data.frequency.find("Weekly") > -1:
			if data.scheduler == day_name:
				print("WEEKLY----"+ data.name)
				objectives = get_objective(data.name)
				print(objectives)

		elif data.frequency.find("Monthly") > -1:
			if data.scheduler == str(day):
				print("MONTHLY----"+ data.name)
				objectives = get_objective(data.name)
				print(objectives)

		elif data.frequency.find("Quarterly") > -1:
			if (month == 'January' or month == 'April' or month == 'July' or month == 'October') and day == 1:
				print("QUARTERLY----"+ data.name)
				objectives = get_objective(data.name)
				print(objectives)

		elif data.frequency.find("Half") > -1:
			if (month == 'January' or month == 'July') and day == 1:
				print("HALF----"+ data.name)
				objectives = get_objective(data.name)
				print(objectives)

		elif data.frequency.find("Yearly") > -1:
			if month == 'January' and day == 1:
				print("YEARLY----"+ data.name)
				objectives = get_objective(data.name)
				print(objectives)