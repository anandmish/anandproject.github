from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Ticket
from rest_framework.response import Response
from .serializers import TicketSerializer, UserSerializer,RegisterSerializer
from django.contrib.auth.models import User
#from rest_framework.authentication import TokenAuthentication
from rest_framework import generics, status
from rest_framework.exceptions import APIException


# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
  #authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated,)
  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (IsAuthenticated,)
  serializer_class = RegisterSerializer

class TICKETListView(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
  #  permission_classes = [IsAuthenticated]
  #  permission_classes = [DjangoModelPermissions]

def get(self, request):
       return self.list(request)
  
class TICKETAddAPIView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


    def post(self, request, *args, **kwargs):

        ticket_serializer = TicketSerializer(data=request.data)
        if ticket_serializer.is_valid():
           ticket_serializer.save()
           return Response({"status": status.HTTP_201_CREATED, "message": " Employee created successfully"})
        return Response(ticket_serializer.errors, status=status.HTTP_201_CREATED) 
       

#class EmployeeDetailView(generics.RetrieveAPIView):
#    queryset = Blog.objects.all()
#    serializer_class = BlogSerializer
  
#    def get_object(self, pk):
#        obj = Blog.objects.filter(id=pk).first()
#        if obj is None:
#            raise APIException({"code": status.HTTP_200_OK, "message": " Record  Does Not Exist"})
#        else:
#            return obj        

     # used  pk to show the particular record.
#    def get(self, request, pk=None):
#        obj = self.get_object(pk)
#        serializer = BlogSerializer(obj)
#        return Response(serializer.data)   



    # update the particular record  through pk
    
class TICKETUpdateView(generics.UpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
   
    def get_object(self, pk):
        obj = Ticket.objects.filter(id=pk).first()
        if obj is None:
            raise APIException({"code": status.HTTP_200_OK, "message": " Record  Does Not Exist"})
        else:
            return obj

    # update the particular record  through pk
    def put(self, request, pk=None):
        obj = self.get_object(pk)
        serializer = TicketSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return Response(serializer.data, status=200)
            return Response({"code": 200, "message": " Update successfully"})
        return Response(serializer.erros, status=status.HTTP_200_OK)
         

class TICKETDeleteView(generics.DestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    
    def get_object(self, pk):
        obj = Ticket.objects.filter(id=pk).first()
        if obj is None:
            raise APIException({"code": status.HTTP_200_OK, "message": " Record  Does Not Exist"})
        else:
            return obj        

    # delete the particular Record of  through pk
    def delete(self, request, pk=None):
        obj = self.get_object(pk)
        obj.delete()
        return Response({"status": status.HTTP_204_NO_CONTENT, "message": " Record deleted successfully"})
          


    



