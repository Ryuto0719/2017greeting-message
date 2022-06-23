
from datetime import datetime

def greet():
    hour = datetime.now().hour
    if hour <= 11:
        message = 'Good morning'+ name + '-san!'
    elif hour <= 17:
        message = 'Hello'+ name + '-san!'
    else:
        message = 'Good evening'+ name + '-san!'

greet('Inoue')
