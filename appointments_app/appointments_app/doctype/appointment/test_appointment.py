# Copyright (c) 2023, Build With Hussain and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestAppointment(FrappeTestCase):
	def test_add_to_appointment_queue(self):
		doctor = frappe.get_doc({"doctype": "Doctor", "first_name": "Test Doctor", "speciality": "Pediatrician"}).insert()
		clinic = frappe.get_doc({"doctype": "Clinic", "name": "Test Clinic", "doctor": doctor.name, "contact_number": "+918770773631"}).insert()
		shift = frappe.get_doc({"doctype": "Schedule Shift", "start_time": "9:00:00", "end_time": "15:00:00", "clinic": clinic.name}).insert()

		day = '2023-07-12'

		appointment = frappe.get_doc({
			"doctype": "Appointment",
			"clinic": clinic.name,
			"shift": shift.name,
			"date": day,
			"patient_name": "Test Patient",
			"contact_number": "+918990886761"
		}).insert()

		self.assertEqual(appointment.queue_number, 1)

		appointment = frappe.get_doc({
			"doctype": "Appointment",
			"clinic": clinic.name,
			"shift": shift.name,
			"date": day,
			"patient_name": "Test Patient",
			"contact_number": "+918990886761"
		}).insert()

		self.assertEqual(appointment.queue_number, 2)
		
	def tearDown(self):
		frappe.db.rollback()