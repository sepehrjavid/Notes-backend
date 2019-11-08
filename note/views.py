from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from note.models import Note
from note.serializers import NoteSerializer


class NoteListCreateView(ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(category_id=self.kwargs.get("category_pk"))


class NoteRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    queryset = Note.objects.all()
