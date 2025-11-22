Step 1: Create Models

Clean, production‑ready models. I’ll define Listing, Booking, and Review with appropriate fields, relationships, and constraints so they’re ready for migrations and API exposure.
⚙️ Key Features

    Listing

        Owner relationship (User).

        Price constraint (>= 0).

        Availability flag.

    Booking

        Linked to both Listing and User.

        Date constraint (check_out > check_in).

        Guests constraint (>= 1).

    Review

        Linked to both Listing and User.

        Rating constraint (1–5).

        Unique constraint: one review per user per listing.

Step 2: Set Up Serializers: listings/serializers.py
scaffold serializers for your Listing and Booking models so they’re ready for DRF endpoints and Swagger documentation.
    ⚙️ Key Features

    ListingSerializer

        Exposes all main fields.

        owner shown as username (read‑only).

    BookingSerializer

        Exposes booking details.

        user shown as username (read‑only).

        Adds listing_title for clarity in Swagger responses.

Step 3: Implement Seeders:

    Create a management command in listings/management/commands/seed.py to populate the database with sample listings data.
    The structure:
    listings/
    management/
        __init__.py
        commands/
            __init__.py
            seed.py

    ⚙️ How It Works

    Ensures a demo user exists (demo_user) to own the listings.

    Seeds the database with 4 sample listings.

    Uses get_or_create to avoid duplicates if you run the command multiple times.

    Prints success/warning messages to the console.
    

