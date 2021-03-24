# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .generator import Csv


@shared_task
def make_csv(schema, rows, pk):
    csv = Csv(schema, rows, pk)
    csv.data_gen()
    print(f'Task {pk} Done')
    return True
