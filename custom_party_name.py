from __future__ import unicode_literals
import frappe
import erpnext
from frappe.model.document import Document
##from frappe.utils import flt


def name(doc,method):
	rows  = 0	
	if doc.party_type == 'Customer':
		datas = frappe.db.sql("""
				select customer_name  from `tabCustomer` 
				where name = %s """,(doc.party))

			
		for i1 in datas:
			for i2 in i1:
				result_data = i2
				result = result_data	
						
				doc.party_name = result
	elif doc.party_type == 'Supplier':
		supplier_datas = frappe.db.sql("""
				select supplier_name  from `tabSupplier` 
				where name = %s """,(doc.party))

			
		for j1 in supplier_datas:
			for j2 in j1:
				result_supdata = j2
				supplier = result_supdata	

				doc.party_name = supplier

	rows +=rows
	

