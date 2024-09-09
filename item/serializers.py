from rest_framework import serializers

from .models import Item


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='item-detail', lookup_field='item_slug')
    # if owner is added then owner will come as "owner": "uttam" otherwise
    # it will come as "owner": <url_of_the_owner>
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Item
        # fields = ['name', 'description', 'price', 'url']
        exclude = ('item_slug', 'created_at')
