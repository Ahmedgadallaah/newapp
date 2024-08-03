import frappe
import json
from frappe.modules.import_file import import_doc

def load_net_contract():
    path = frappe.get_app_path('newapp', 'newapp', 'doctype', 'net_contract', 'net_contract.json')
    with open(path) as jsonfile:
        doc = json.load(jsonfile)
        import_doc(doc)

if __name__ == "__main__":
    load_net_contract()