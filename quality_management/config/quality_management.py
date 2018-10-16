from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
        {
            "label": "Goal and Procedure",
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
            "label": "Review and Action",
            "items": [
                {
                    "type": "doctype",
                    "name": "Quality Review"
                },
                {
                    "type": "doctype",
                    "name": "Quality Action"

                }
            ]
        },
        {
            "label": "Meeting",
            "items": [
                {
                    "type": "doctype",
                    "name": "Quality Meeting"

                }
            ]
        },
        {
            "label": "Feedback",
            "items": [
                {
                    "type": "doctype",
                    "name": "Customer Feedback"

                },
                {
                    "type": "doctype",
                    "name": "Feedback Template"

                }
            ]
        },
    ]