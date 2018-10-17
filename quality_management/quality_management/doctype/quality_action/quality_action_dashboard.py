from frappe import _

def get_data():
    #try multipe for customer feedback or review
    return {
        'fieldname': 'review',
        'transactions': [
            {
                'label': _('Dummy'),
                'items': ['Quality Review']
            }
        ],
    }