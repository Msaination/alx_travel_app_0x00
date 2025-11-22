from rest_framework import serializers
from .models import Listing, Booking


class ListingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # show username instead of ID

    class Meta:
        model = Listing
        fields = [
            'id',
            'title',
            'description',
            'location',
            'price_per_night',
            'available',
            'created_at',
            'updated_at',
            'owner',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'owner']


class BookingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')  # show username instead of ID
    listing_title = serializers.ReadOnlyField(source='listing.title')  # helpful for Swagger

    class Meta:
        model = Booking
        fields = [
            'id',
            'listing',
            'listing_title',
            'user',
            'check_in',
            'check_out',
            'guests',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at', 'user', 'listing_title']
