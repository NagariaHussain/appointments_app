# Copyright (c) 2023, Build With Hussain and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from frappe.utils import format_time


class ScheduleShift(Document):
	def before_save(self):
		# set the title field to "start_time-end_time"
		self.title = (
			format_time(self.start_time, "HH:mm") + "-" + format_time(self.end_time, "HH:mm")
		)
