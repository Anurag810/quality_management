from frappe import _

def get_data():
    return {
        'fieldname': 'description',
        'transactions': [
            {
                'label': _('Dummy'),
                'items': ['Customer Feedback']
            }
        ],
    }