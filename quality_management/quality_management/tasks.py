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
		for objective in objectives:
			values = objective.objective
			target = objective.target
			unit = objective.unit
		print(values)
		print(target)
		print(unit)
		"""doc = frappe.get_doc({
			"doctype": "Quality Review",
   			"goal": name,
   			"date": frappe.utils.nowdate(),
   			"values":	[{
    			"objective": kwargs.get, 
    			"target":,
    			"target_unit":,
				"achieved_unit"
    		}]
   		})"""
		return objectives

	for data in frappe.get_all("Quality Goal",fields=['name','scheduler','frequency']):
		if data.frequency == 'Daily':
			print("EVERYDAY----"+ data.name)
			objectives = get_objective(data.name)
			#print(objectives)

		elif data.frequency == 'Weekly':
			print("WEEKLY----"+ data.name)
			print(data.weekly == day_name)
			print(data.weekly)
			print(day_name)
			if data.weekly == day_name:
				print("WEEKLY----"+ data.name)
				objectives = get_objective(data.name)
			#	print(objectives)

		elif data.frequency == 'Monthly':
			if data.monthly == str(day):
				print("MONTHLY----"+ data.name)
				objectives = get_objective(data.name)
			#	print(objectives)

		elif data.frequency == 'Quartely':
			if (month == 'January' or month == 'April' or month == 'July' or month == 'October') and day == 1:
				print("QUARTERLY----"+ data.name)
				objectives = get_objective(data.name)
			#	print(objectives)

		elif data.frequency == 'Half Yearly':
			if (month == 'January' or month == 'July') and day == 1:
				print("HALF----"+ data.name)
				objectives = get_objective(data.name)
			#	print(objectives)

		elif data.frequency == 'Yearly':
			if month == 'January' and day == 1:
				print("YEARLY----"+ data.name)
				objectives = get_objective(data.name)
			#	print(objectives)