from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from .tasks import make_csv
from .models import *
from .forms import *


class List(ListView):
    model = Schema


class Add(LoginRequiredMixin, CreateView):
    model = Schema
    fields = ["name"]


class DataList(ListView):
    model = Data

    def get_queryset(self):
        new_context = Data.objects.filter(
            schema__pk=self.kwargs["pk"],
        )
        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['schema'] = Schema.objects.get(pk=self.kwargs["pk"])
        return context


class AddData(LoginRequiredMixin, CreateView):
    model = Data
    form_class = DataForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['schema'] = Schema.objects.get(pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        schema = Schema.objects.get(pk=self.kwargs["pk"])
        if schema:
            form.instance.schema = schema
            valid = super().form_valid(form)
            make_csv.delay(schema.id, form.instance.count, form.instance.id)
            return valid
        else:
            form.add_error('order', 'Error selected Schema'
                                    ' Please choose another.')


class Detail(DetailView):
    model = Schema


class Delete(LoginRequiredMixin, DeleteView):
    model = Schema
    success_url = reverse_lazy('list')


class AddColumn(LoginRequiredMixin, CreateView):
    model = Column
    form_class = ColumnForm

    def form_valid(self, form):
        schema = Schema.objects.get(pk=self.kwargs["pk"])
        order = form.instance.order
        try:
            # Check if this order number is not used by other column
            Column.objects.get(schema=schema, order=order)
            form.add_error('order', 'Some other column already uses this order number.'
                                    ' Please choose another on.')
            return self.form_invalid(form)
        except Exception:
            pass
        form.instance.schema = schema
        return super().form_valid(form)


class ColumnDelete(LoginRequiredMixin, DeleteView):
    model = Column

    def get_success_url(self, **kwargs):
        column = Column.objects.get(pk=self.kwargs["pk"])
        schema = Schema.objects.get(column=column)
        return reverse_lazy('detail', kwargs={'pk': schema.pk})
