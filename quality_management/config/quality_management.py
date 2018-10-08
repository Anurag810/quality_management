from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
        {
            "label": "DUMMY 1",
            "items": [
                {
                    "type": "doctype",
                    "name": "Quality Goal"
                },
                {
                    "type": "doctype",
                    "name": "Quality Procedure"
                }
            ]
        },
        {
            "label": "DUMMY 2",
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
            "label": "DUMMY 3",
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
            "label": "DUMMY 4",
            "items": [
                {
                    "type": "doctype",
                    "name": "Customer Feedback"

                }
            ]
        }
    ]