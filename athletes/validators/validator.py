from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.core.exceptions import ValidationError

def validate_date_of_birth(date_of_birth):
    now = datetime.now()
    changing_cat_date = datetime(now.year, 12, 31)

    time_difference = relativedelta(changing_cat_date, date_of_birth)
    years = time_difference.years
    if years < 7:
        raise ValidationError(
            '%d years is not permitted. Above 7' % years
        )

    return date_of_birth