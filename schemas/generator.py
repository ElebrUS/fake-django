from .models import Schema, Data
from django.conf import settings
from celery import shared_task
from faker import Faker
import pandas as pd
import io
import boto3


class Csv:
    def __init__(self, schema, rows, pk):
        self.Schema = Schema.objects.get(id=schema)
        self.columns = self.Schema.column.order_by("order")
        self.rows = int(rows)
        self.Data = Data.objects.get(id=pk)
        self.fake = Faker()

    def data_gen(self):
        head, data = self.serialize()
        csv_text = self.fake.dsv(header=head, data_columns=data, num_rows=self.rows, delimiter=',')
        text = io.StringIO(csv_text)
        csv = io.StringIO()
        df = pd.read_csv(text, sep=",", index_col=head[0])
        df.to_csv(csv)
        filename = f'result_{self.Data.id}.csv'
        session = boto3.Session(
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
        )
        s3 = session.resource('s3')
        obj = s3.Object(settings.AWS_STORAGE_BUCKET_NAME, 'media/' + filename)
        obj.put(Body=csv.getvalue(), Key='media/' + filename)
        url = settings.MEDIA_URL + filename
        self.Data.status = True
        self.Data.url = str(url)
        self.Data.save()
        return str(url)

    def serialize(self):
        data = []
        head = []
        for idc, column in enumerate(self.columns):
            if column.range_min and column.range_max is not None:
                if str(column.data_type) == 'integer':
                    data.append("{{pyint:range" + str(idc) + "}}")
                    self.fake.set_arguments('range' + str(idc),
                                            {'min_value': column.range_min, 'max_value': column.range_max})
                elif str(column.data_type) == 'text':
                    data.append("{{paragraph:range" + str(idc) + "}}")
                    self.fake.set_arguments('range' + str(idc),
                                            {'nb_sentences': (column.range_max + column.range_min) / 2})
                else:
                    data.append("{{" + str(column.data_type) + "}}")
            else:
                if str(column.data_type) == 'integer':
                    data.append("{{pyint}}")
                else:
                    data.append("{{" + str(column.data_type) + "}}")
            head.append(column.name)
        return tuple(head), tuple(data)
