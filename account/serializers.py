from rest_framework import serializers
from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # lookup_field can be added to mention field on which relation will be created
    items = serializers.HyperlinkedRelatedField(many=True, read_only=True,
                                                view_name='item-detail', lookup_field='item_slug')
    # password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'url', 'items', 'email', 'is_staff']


class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
