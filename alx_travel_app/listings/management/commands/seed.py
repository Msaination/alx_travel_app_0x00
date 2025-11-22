from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing
import random
from django.contrib.auth import get_user_model



class Command(BaseCommand):
    help = "Seed the database with sample listings data"

    def handle(self, *args, **kwargs):
        User = get_user_model()  # ✅ now defined

        user, _ = User.objects.get_or_create(
            username="demo_user",
            defaults={"email": "demo@example.com"}
        )

        sample_listings = [
            {
                "title": "Luxury Beachfront Villa",
                "description": "A stunning villa with ocean views and private pool.",
                "location": "Cape Town, South Africa",
                "price_per_night": 250.00,
            },
            {
                "title": "Cozy Mountain Cabin",
                "description": "Perfect getaway in the Drakensberg mountains.",
                "location": "KwaZulu-Natal, South Africa",
                "price_per_night": 120.00,
            },
            {
                "title": "City Apartment",
                "description": "Modern apartment in the heart of Johannesburg.",
                "location": "Johannesburg, South Africa",
                "price_per_night": 90.00,
            },
            {
                "title": "Safari Lodge",
                "description": "Experience wildlife up close in Kruger National Park.",
                "location": "Mpumalanga, South Africa",
                "price_per_night": 300.00,
            },
        ]

        for data in sample_listings:
            listing, created = Listing.objects.get_or_create(
                title=data["title"],
                defaults={
                    "description": data["description"],
                    "location": data["location"],
                    "price_per_night": data["price_per_night"],
                    "available": True,
                    "owner": user,
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created listing: {listing.title}"))
            else:
                self.stdout.write(self.style.WARNING(f"Listing already exists: {listing.title}"))

        self.stdout.write(self.style.SUCCESS("Database seeding complete!"))
