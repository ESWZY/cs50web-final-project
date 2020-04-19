#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "airline.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

# python manage.py makemigrations
# check if has modified

# python manage.py migrate
# apply all migration

#python manage.py shell
# f = Flight(origin="NY", destination="LD", duration=415)
# f.save()
# Flight.objects.all()
# jfk.departures.all()

# python manage.py createsuperuser