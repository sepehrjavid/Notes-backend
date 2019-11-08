from django.urls import path, re_path

from note.views import NoteListCreateView, NoteRetrieveUpdateDestroyView

app_name = "Notes"

urlpatterns = [
    re_path(r'^noteListCreate/(?P<category_pk>\d+)$', NoteListCreateView.as_view()),
    re_path(r'^noteRetrieveUpdateDestroy/(?P<pk>\d+)$', NoteRetrieveUpdateDestroyView.as_view())
]
