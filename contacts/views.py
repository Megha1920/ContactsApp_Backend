from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
# Create your views here.
from rest_framework import viewsets, permissions
from .models import Contact
from .serializers import ContactSerializer

class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Contact.objects.filter(user=self.request.user)
        print(f"Queryset: {queryset}")  # Add logging
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Contact successfully deleted."}, status=status.HTTP_204_NO_CONTENT)
