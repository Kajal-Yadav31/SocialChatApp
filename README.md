# SocialDj - Your Social Media Hub

## Demo



## Overview
SocialDj is a dynamic social media platform developed with Django framework, enabling users to connect, share, and interact online. The website incorporates essential features such as secure authentication, user profile management with editing capabilities, seamless post creation with image selection from Flickr, and interactive engagement through likes, comments, and replies. Additionally, the platform offers a real-time chatting inbox, fostering communication and networking among registered users.


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
   - Users can delete and edit his/her post.

4. **Social Interaction:**
   - Implemented features for users to like, comment on, and reply to specific posts .
   - Encourages social engagement and interaction among users within the platform.

5. **Chatting Inbox:**
   - SocialDj provides a dedicated chatting inbox page where registered users can communicate with each other.
   - The chat functionality is implemented using Django Channels and WebSockets, ensuring real-time communication and seamless user experience.

## Getting Started

### Clone the Repository

1) First, clone the repository to your local machine:

git clone https://github.com/Kajal-Yadav31/SocialChatApp.git


2) cd `SocialChatApp`


## Docker Setup

### Prerequisites
- Docker installed on your machine. You can download and install Docker from [here](https://www.docker.com/get-started).

### Running the project

1) To Build and Start the Docker Container :
    `docker-compose up -d`

2) Apply Migrations :
   ` docker-compose exec web python manage.py migrate`

3) Create a Superuser :to access admin panel
    `docker-compose exec web python manage.py createsuperuser`


### Usage
- Access the application at `http://localhost:8000/` in your web browser.
- Register an account, verify your email, and start creating your posts.
- Explore the features such as post like, create, comment, reply and delete.

## License
This project is licensed under the [MIT License]


## Contact
For inquiries or issues, contact [kajalyadav070496@gmail.com].
