from rest_framework import serializers
from Authentication_Module_backend_app.models import users

class usersserializer(serializers.ModelSerializer):
    class Meta:
        model=users
        fields='__all__'
