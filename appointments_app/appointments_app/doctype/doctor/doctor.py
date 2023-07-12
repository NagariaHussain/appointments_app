# Copyright (c) 2023, Build With Hussain and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Doctor(Document):
	def validate(self):
		self.set_full_name()

	def set_full_name(self):
		self.full_name = (
			(self.first_name + " " + self.last_name) if self.last_name else self.first_name
		)
