from datetime import date
from students.models import AcademicYear


def register_academic_year():
    current_year = date.today().year
    next_year = current_year + 1
    academic_year, created = AcademicYear.objects.get_or_create(
        from_date=date(current_year, 1, 1),
        to=date(next_year, 1, 1)
    )



    return academic_year
