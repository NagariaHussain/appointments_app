# Copyright (c) 2023, Build With Hussain and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase
from appointments_app.appointments_app.doctype.appointment_queue.appointment_queue import create_queues_for_today


class TestAppointmentQueue(FrappeTestCase):
	def test_create_queues_for_today(self):
		# create test records
		doctor = frappe.get_doc({"doctype": "Doctor", "first_name": "Test Doctor", "speciality": "Pediatrician"}).insert()
		clinic = frappe.get_doc({"doctype": "Clinic", "name": "Test Clinic", "doctor": doctor.name, "contact_number": "+918770773631", "is_published": True}).insert()
		test_shift1 = frappe.get_doc({"doctype": "Schedule Shift", "start_time": "9:00:00", "end_time": "15:00:00", "clinic": clinic.name}).insert()
		test_shift2 = frappe.get_doc({"doctype": "Schedule Shift", "start_time": "16:00:00", "end_time": "20:00:00", "clinic": clinic.name}).insert()

		# assert no queues exist
		self.assertEqual(frappe.db.count("Appointment Queue"), 0)

		create_queues_for_today()

		# assert exactly one queue exists
		self.assertEqual(frappe.db.count("Appointment Queue"), 2)

		# and that queue is for the above clinic and shift and today's date
		queue = frappe.get_doc("Appointment Queue", {"clinic": clinic.name, "shift": test_shift1.name, "date": frappe.utils.today()})
		self.assertTrue(queue)

	def tearDown(self):
		frappe.db.rollback()