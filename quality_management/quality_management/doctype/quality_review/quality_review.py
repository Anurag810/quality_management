# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class QualityReview(Document):
	
	def before_save(self):
	#	print(self.values[0].objective)
	#	print(self.values[0].achieved)
	#	print(self.values[0].target)
	#	print(len(self.values))
		for value in self.values:
			if value.achieved < value.target:
				print(value.objective)
				print(value.achieved)
				print(value.target)
