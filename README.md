AIRBNB CLONE PROJECT

OVERVIEW

This project is an Airbnb clone aimed at providing a platform for users to list, discover, and book accommodations worldwide. The project focuses on creating a web application with functionalities similar to Airbnb, including user authentication, property listings, search and filtering, booking management, payment processing, messaging system, user reviews, and an admin panel.

FEATURES

User Authentication: Users can register, log in, and log out securely.
Property Listings: Hosts can create, edit, and manage listings for their properties.
Search and Filter: Guests can search for properties based on various criteria such as location, dates, price range, and amenities.
Booking Management: Guests can book properties for specific dates, and hosts can manage bookings.
Payment Processing: Integration with a payment gateway for secure transactions.
Messaging System: Communication between hosts and guests through a messaging system.
User Reviews and Ratings: Guests can leave reviews and ratings for properties they've booked.
Admin Panel: Site administrators can manage users, listings, bookings, payments, etc.
Responsive Design: Accessible and user-friendly design across devices.
Security: Implementation of security measures to protect user data and prevent unauthorized access.

SETUP

1. Clone the repository to your local machine:

git clone https://github.com/your-username/airbnb-clone.git

2. Install project dependencies:

pip install -r requirements.txt

3. Set up database migrations:

python manage.py makemigrations
python manage.py migrate

4. Run the development server:

python manage.py runserver

Access the application in your web browser at http://localhost:8000.
	
This project is licensed under the MIT License - see the LICENSE file for details.
