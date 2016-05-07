from django.shortcuts import render
from .models import StoredImage

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework import generics

from .serializers import StoredImageSerializer
from .permissions import IsOwner


import os
from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper
#TO DO: Fix error messages when objects don't exist
class DownloadView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated, IsOwner, )
    authentication_classes = (SessionAuthentication,)
    def get(self, request, pk):
        """
        Send back a file.
        """
        filename = StoredImage.objects.filter(id=pk, owner=request.user)[0].image.path
        wrapper = FileWrapper(StoredImage.objects.filter(id=9, owner=request.user)[0].image.file)
        response = HttpResponse(wrapper, content_type='image')
        response['Content-Length'] = os.path.getsize(filename)
        #replace attachment with inline to get browser to display image
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(filename)
        return response


class ImageViewSet(viewsets.ModelViewSet):
    """
    Set of views that allows images to be viewed, created, or destroyed.
    """
    queryset = StoredImage.objects.all()
    serializer_class = StoredImageSerializer
    #not allowing PUT right now because the old image won't be deleted
    http_method_names = ['post', 'head', 'options', 'get', 'delete']
    permission_classes = (IsAuthenticated, IsOwner, )
    authentication_classes = (SessionAuthentication,)
    
    def get_queryset(self):
         """
         Only list images that belong to the user.
         """
         return StoredImage.objects.filter(owner=self.request.user)
   
    def perform_create(self, serializer):
         """
         Modify the create process to add the user as a foreign key to image.
         """
         serializer.save(owner=self.request.user)

