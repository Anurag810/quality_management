from frappe import _

def get_data():
    return {
        'fieldname': 'quality_review',
        'transactions': [
            {
                'label': _('Dummy'),
                'items': ['ToDo', 'Note']
            }
        ],
    }