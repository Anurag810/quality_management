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
		doc = frappe.get_doc({
			"doctype": "Quality Review",
   			"goal": name,
   			"date": frappe.utils.nowdate(),
		})
		#enter child table values
		"""for objective in objectives:
			doc.append("values",{
				'objective': objective.objective,
				'target': objective.target,
				'target_unit': objective.unit,
				'achieved_unit': objective.unit
			})"""
		doc.insert()
		frappe.db.commit()
		return objectives

	for data in frappe.get_all("Quality Goal",fields=['name','frequency','date','weekly']):
		if data.frequency == 'Daily':
			objectives = get_objective(data.name)
			print(objectives)

		elif data.frequency == 'Weekly':
			if data.weekly == day_name:
				objectives = get_objective(data.name)
				print(objectives)

		elif data.frequency == 'Monthly':
			if data.date == str(day):
				objectives = get_objective(data.name)
				print(objectives)

		elif data.frequency == 'Quarterly':
			if (month == 'January' or month == 'April' or month == 'July' or month == 'October') and str(day) == data.date:
				objectives = get_objective(data.name)
				print(objectives)

		elif data.frequency == 'Half Yearly':
			if (month == 'January' or month == 'July') and str(day) == data.date:
				objectives = get_objective(data.name)
				print(objectives)

		elif data.frequency == 'Yearly':
			if month == data.yearly and str(day) == data.date:
				objectives = get_objective(data.name)
				print(objectives)