from django.db import models
from django.contrib.auth.models import User


class Listing(models.Model):
    """Represents a travel listing (e.g., hotel, tour, rental)."""
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Owner of the listing (e.g., host or admin)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")

    class Meta:
        ordering = ["-created_at"]
        constraints = [
            models.CheckConstraint(check=models.Q(price_per_night__gte=0), name="price_non_negative"),
        ]

    def __str__(self):
        return f"{self.title} - {self.location}"


class Booking(models.Model):
    """Represents a booking made for a listing."""
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bookings")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        constraints = [
            models.CheckConstraint(check=models.Q(guests__gte=1), name="guests_min_one"),
            models.CheckConstraint(check=models.Q(check_out__gt=models.F("check_in")), name="valid_booking_dates"),
        ]

    def __str__(self):
        return f"Booking by {self.user.username} for {self.listing.title}"


class Review(models.Model):
    """Represents a review left by a user for a listing."""
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveSmallIntegerField()  # 1–5 stars
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        constraints = [
            models.CheckConstraint(check=models.Q(rating__gte=1) & models.Q(rating__lte=5), name="valid_rating_range"),
            models.UniqueConstraint(fields=["listing", "user"], name="unique_review_per_user"),
        ]

    def __str__(self):
        return f"Review {self.rating}/5 by {self.user.username} for {self.listing.title}"

