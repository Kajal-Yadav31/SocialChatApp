# SocialDj - Your Social Media Hub

## Overview
SocialDj is a dynamic social media platform developed with Django framework, enabling users to connect, share, and interact online. The website incorporates essential features such as secure authentication, user profile management with editing capabilities, seamless post creation with image selection from Flickr, and interactive engagement through likes, comments, and replies. Additionally, the platform offers a real-time chatting inbox, fostering communication and networking among registered users. 


## Demo


## Features

1. **Authentication and Account Management:**
   - Implemented user authentication using Django custom models.
   - Included email verification functionality to ensure secure user registration.
   - Implemented features for forgot password and reset password for enhanced user experience and security.

2. **Profile Management:**
   - Automatically creates user profiles upon registration using Django signals.
   - Users can edit their profiles, including changing name, uploading a photo, adding bio, and specifying location.
   - Dedicated "My Profile" page allows users to view and manage their profiles conveniently.

3. **Post Creations**
   - Users can create posts by selecting pictures from Flickr.com.
   - Utilized Beautiful Soup in Python to fetch photos from Flickr.
   - Users can add captions and specify categories for their posts to organize content effectively.

4. **Social Interaction:**
   - Implemented features for users to like, comment on, and reply to specific posts.
   - Encourages social engagement and interaction among users within the platform.

5. **Chatting Inbox:**
   - SocialDj provides a dedicated chatting inbox page where registered users can communicate with each other.
   - The chat functionality is implemented using Django Channels and WebSockets, ensuring real-time communication and seamless user experience.

## Getting Started

### Prerequisites
- Python 3.11.2
- Django 4.2.1
- Additional dependencies are mention in the requirement.txt file

### Installation
1. Clone the repository: `git clone https://github.com/Kajal-Yadav31/`
2. Navigate to the project directory: `r`
3. Install dependencies: `pip install -r requirements.txt`
4. Apply migrations: `python manage.py migrate`
5. Run the development server: `python manage.py runserver`

### Usage
- Access the application at `http://localhost:8000/` in your web browser.
- Register an account, verify your email, and start creating your posts.
- Explore the features such as post like, create, comment, reply and delete.

## License
This project is licensed under the [MIT License]


## Contact
For inquiries or issues, contact [kajalyadav3107@gmail.com].
