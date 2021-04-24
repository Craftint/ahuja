from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import today
import json
from frappe.desk.reportview import get_filters_cond
from functools import partial
#from toolz import groupby, merge, valmap, compose, get, excepts, first, pluck

from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

@frappe.whitelist()
def address_details(doc,handler=""):
    oc = frappe.get_doc('Supplier',doc.supplier)
    oc.phone = doc.phone
    oc.email = doc.email
    oc.shipping_address = doc.ship_address
    oc.billing_address = doc.billing_address
    oc.save()




@frappe.whitelist()
def address_details_customer(doc,handler=""):
    oc = frappe.get_doc('Customer',doc.customer)
    oc.phone = doc.phone
    oc.email = doc.email
    oc.shipping_address = doc.ship_address
    oc.billing_address = doc.billing_address
    oc.save()


