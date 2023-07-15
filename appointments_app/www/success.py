import frappe


def get_context(context):
    context.no_cache = 1
    context.queue_number = frappe.cache.get_value(f"{frappe.session.sid}:queue_number")
    