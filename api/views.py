from rest_framework.response import Response
from rest_framework.decorators import api_view
from Authentication_Module_backend_app.models import users
from .serializers import usersserializer


@api_view(['GET'])
def getusers(request):
    users_data=users.objects.all()
    serializer=usersserializer(users_data, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def adduser(request):
    serializer=usersserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()    
    return Response(serializer.data)