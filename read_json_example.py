import json
from datetime import datetime

with open("document.json", "r") as file:
    json_data = json.load(file)

payee_id = json_data.get("payee").get("id")
print("Payee ID:", payee_id)

invoices_with_583 = [invoice for invoice in json_data.get("invoiceIds") if "583" in invoice]
print("Invoices containing '583':", invoices_with_583)

json_data["claimDateTime"] = datetime.fromtimestamp(json_data["claimDateTime"] / 1e3).strftime('%Y-%m-%dT%H:%M:%S')
json_data["fileDateTime"] = datetime.fromtimestamp(json_data["fileDateTime"] / 1e3).strftime('%Y-%m-%dT%H:%M:%S')
json_data["receivedDateTime"] = datetime.fromtimestamp(json_data["receivedDateTime"] / 1e3).strftime('%Y-%m-%dT%H:%M:%S')

with open("modified_document.json", "w") as file:
    json.dump(json_data, file, indent=4)

print("Modified JSON document has been written to 'modified_document.json'.")
