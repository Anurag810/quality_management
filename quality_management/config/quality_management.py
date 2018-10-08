from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
        {
            "label": "QMS1",
            "items": [
                {
                    "type": "doctype",
                    "name": "Quality Goal"
                }
            ]
        },
        {
            "label": "QMS2",
            "items": [
                {
                    "type": "doctype",
                    "name": "Quality Review"
                },
                {
                    "type": "doctype",
                    "name": "Quality Procedure"
                },
                {
                    "type": "doctype",
                    "name": "Customer Feedback"

                },
                {
                    "type": "doctype",
                    "name": "Quality Action"

                },
                {
                    "type": "doctype",
                    "name": "Quality Audit"
                },
                {
                    "type": "doctype",
                    "name": "Quality Audit Type"

                },
                {
                    "type": "doctype",
                    "name": "Quality Monitoring Frequency"

                }
            ]
        }
    ]