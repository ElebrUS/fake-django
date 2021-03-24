from django.db import models
from django.urls import reverse


class Schema(models.Model):
    name = models.CharField(max_length=80)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})


class DataType(models.Model):
    type = models.CharField(max_length=80)

    def __str__(self):
        return self.type


class Column(models.Model):
    name = models.CharField(max_length=80)
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE, related_name="column")
    order = models.IntegerField()
    data_type = models.ForeignKey(DataType, on_delete=models.CASCADE)
    range_min = models.IntegerField(default=0, blank=True)
    range_max = models.IntegerField(default=0, blank=True)

    class Meta:
        unique_together = ('schema', 'order',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.schema.pk})


class Data(models.Model):
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    url = models.FileField(blank=True, null=True)

    class Meta:
        verbose_name = 'Data Set'
        verbose_name_plural = 'Data Sets'
        ordering = ['-id']

    def __str__(self):
        return '{} > {}'.format(self.schema.name, self.count)

    def get_absolute_url(self):
        return reverse('data-set', kwargs={'pk': self.schema.pk})
