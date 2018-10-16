from frappe import _

def get_data():
    #try multipe for customer feedback or review
    return {
        'fieldname': 'goal',
        'transactions': [
            {
                'label': _('Dummy'),
                'items': ['']
            }
        ],
    }