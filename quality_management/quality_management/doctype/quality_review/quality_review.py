# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class QualityReview(Document):	

	def after_insert(self):
		problem = ''
		for value in self.values:
			if int(value.achieved) < int(value.target):
				problem = problem + 'In '+ value.objective +', the Achieved Value '+ str(value.achieved) +' is less than the Target Value '+ str(value.target) +'\n'

		if(problem != ''):
			problem = filter(None, problem.split("\n"))
			doc = frappe.get_doc({
				'doctype': 'Quality Action',
				'action': 'Corrective',
				'type': 'Quality Review',
				'review': ''+ self.name +'',
				'date': ''+ frappe.utils.nowdate() +''
			})
			for data in problem:
				doc.append("description",{
					'problem': data
				})
			#doc.save()
			doc.insert()
			frappe.db.commit()
		
		#query = frappe.get_list("Quality Action", filters={"review":""+ self.name +""})
		#if len(query) == 0:
		#	for value in self.values:
		#		if int(value.achieved) < int(value.target):
		#			problem = problem + 'In '+ value.objective +', the Achieved Value '+ str(value.achieved) +' is less than the Target Value '+ str(value.target) +'\n'

		#	if(problem != ''):
		#		problem = filter(None, problem.split("\n"))
		#		print(problem)
				#doc = frappe.get_doc({
				#	'doctype': 'Quality Action',
				#	'action': 'Corrective',
				#	'type': 'Quality Review',
				#	'review': ''+ self.name +'',
				#	'date': ''+ frappe.utils.nowdate() +''
				#})
				#for data in problem:
				#	doc.append("description",{
				#		'problem': data
				#	})
				#doc.save()
				#doc.insert()
				#frappe.db.commit()
		#else:
		#	pass

	def on_update(self):
		print("On Update")
		problem = ''
		for value in self.values:
			if int(value.achieved) < int(value.target):
				problem = problem + 'In '+ value.objective +', the Achieved Value '+ str(value.achieved) +' is less than the Target Value '+ str(value.target) +'\n'

		if problem != '':
			pass

		else:
			pass
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
				
		
		#	query = frappe.get_list("Quality Action", filters={"review":""+ self.name +""})
		#	print(self.name)
		#	if len(query) != 0:
		#		print(query[0].name)
		#		print("In If")
		#		for value in self.values:
		#			if int(value.achieved) < int(value.target):
		#				problem = problem + 'In '+ value.objective +', the Achieved Value '+ str(value.achieved) +' is less than the Target Value '+ str(value.target) +'\n'
#
#				if problem != '':
#					problem = filter(None, problem.split("\n"))
#					print(problem)
#					doc = frappe.delete_doc("Quality Action Table", filters={'parent': ''+ query[0].name +''})
#					doc = frappe.get_doc("Quality Action", ""+ query[0].name +"")
#					for data in problem:
#						doc.append("description",{
#							'problem': data
#						})
#					doc.save
#					frappe.db.commit()
	#				query = frappe.db.sql("""UPDATE `tabQuality Action` SET problem='"""+ problem +"""' WHERE review='"""+self.name+"""'""")
#				else:
#					frappe.delete_doc("Quality Action", ""+ query[0].name +"")
	#				query = frappe.db.sql("""DELETE FROM `tabQuality Action` WHERE review='"""+self.name+"""'""")
#			else:
#				pass
#		else:
#			pass