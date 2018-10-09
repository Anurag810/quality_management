from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
        {
            "label": "Quality Goal and Procedure",
            "items": [
                {
                    "type": "doctype",
                    "name": "Quality Goal"
                },
                {
                    "type": "doctype",
                    "name": "Quality Procedure"
                },
                {
                    "type": "doctype",
                    "name": "Measurement Unit"
                }
            ]
        },
        {
            "label": "Quality Review and Action",
            "items": [
                {
                    "type": "doctype",
                    "name": "Quality Review"
                },
                {
                    "type": "doctype",
                    "name": "Quality Action"

                },
                {
                    "type": "doctype",
                    "name": "Quality Monitoring Frequency"

                }
            ]
        },
        {
            "label": "Quality Audit",
            "items": [
                {
                    "type": "doctype",
                    "name": "Quality Audit"
                },
                {
                    "type": "doctype",
                    "name": "Quality Audit Type"

                }
            ]
        },
        {
            "label": "Quality Feedback",
            "items": [
                {
                    "type": "doctype",
                    "name": "Customer Feedback"

                }
            ]
        }
    ]