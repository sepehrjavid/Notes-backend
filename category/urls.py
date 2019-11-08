from django.urls import path, re_path

from category.views import CategoryListCreateView, CategoryUpdateDestroy

app_name = "category"

urlpatterns = [
    path('categoryListCreate', CategoryListCreateView.as_view()),
    re_path(r'^categoryUpdateDestroy/(?P<pk>\d+)$', CategoryUpdateDestroy.as_view())
]
