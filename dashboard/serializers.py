from rest_framework import serializers
from accounts.models import Profile

class NewRegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'