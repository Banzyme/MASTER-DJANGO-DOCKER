import os
from twistapp.models import *
from postgres_copy import CopyMapping
from django.core.management.base import BaseCommand

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        c = CopyMapping(
            # Model name
            AllResults,
            # The path to your CSV
            './twistapp/static/data/matricgov.csv',
            # And a dict mapping the  model fields to CSV column titles
            dict(wrote='Wrote', passed='Passed', year='Year', name='Name'),
        )
        # Then save it.
        c.save()