from datetime import datetime

def default_parameters(request):
    return {
        'year' : datetime.now().year,
    }