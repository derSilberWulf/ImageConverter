from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper


from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework import generics

from .serializers import StoredImageSerializer
from .permissions import IsOwner
from .models import StoredImage
from .imagefunctions import modifyImage
import os



class ImageModifierView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated, IsOwner, )
    authentication_classes = (SessionAuthentication,)
    http_method_names = ['get', 'post']
    
    def get(self, request):
        template = loader.get_template('converter/editImage.html')
        ownedImages = StoredImage.objects.filter(owner=request.user)
        functionlist = ['invert', 'addalpha']
        context = {
                   'imagelist' : ownedImages,
                   'functionlist' : functionlist
                   }
        return HttpResponse(template.render(context, request))
        
    def post(self, request):
        pk = int(request.POST.get('image_id'))
        arguments = request.POST.dict()#dict(request.POST.iterlists())
        user_image = get_object_or_404(StoredImage, owner=request.user, id=pk)
        imgpath = user_image.image.path
        modifyImage(imgpath, ['remove_red'], arguments)
        return redirect('download', pk=pk)
        

class DownloadView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated, IsOwner, )
    authentication_classes = (SessionAuthentication,)
    http_method_names = ['get']
    def get(self, request, pk):
        """
        Send back a file. Only allow files that belong to the requester.
        """
        user_image = get_object_or_404(StoredImage, owner=request.user, id=pk)
        filename = user_image.image.path
        wrapper = FileWrapper(user_image.image.file)
        response = HttpResponse(wrapper, content_type='image')
        response['Content-Length'] = os.path.getsize(filename)
        #replace attachment with inline to get browser to display image
        #response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(filename)
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(filename)
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

