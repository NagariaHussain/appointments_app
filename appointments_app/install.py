import frappe


def after_install():
	frappe.db.set_single_value("Website Settings", "website_theme", "JDP Doctors")
	frappe.db.set_single_value("Website Settings", "address", "Made with 💖 in Jagdalpur, by Hussain")