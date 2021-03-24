from django.urls import path
from .views import *

urlpatterns = [
    path('', List.as_view(template_name="list.html"), name="list"),
    path('new/', Add.as_view(template_name="add.html"), name="create"),
    path('<int:pk>/detail/', Detail.as_view(template_name="detail.html",), name="detail"),
    path('<int:pk>/delete/', Delete.as_view(template_name="delete.html"), name="delete"),
    path('<int:pk>/delete_col/', ColumnDelete.as_view(template_name="col_delete.html"), name="delete_col"),
    path('<int:pk>/add/', AddColumn.as_view(template_name="add_column.html"), name="column-create"),
    path('<int:pk>/data/', DataList.as_view(template_name="data.html"), name="data-set"),
    path('<int:pk>/data/add/', AddData.as_view(template_name="add_data.html"), name="data-add"),
]