# SocialDj - Your Social Media Hub

## Demo

### ScreenShots of project:
![Screenshot 2024-06-28 112400](https://github.com/Kajal-Yadav31/SocialChatApp/assets/129850619/8c68decd-82e9-4f2d-868b-fcd803b79d4c)

![Screenshot 2024-06-28 112415](https://github.com/Kajal-Yadav31/SocialChatApp/assets/129850619/90157362-307b-46b6-9da5-37b41361cacf)

![Screenshot 2024-06-28 112429](https://github.com/Kajal-Yadav31/SocialChatApp/assets/129850619/cda51e61-6764-460c-af6f-4f518ebf3bca)

![Screenshot 2024-06-28 112509](https://github.com/Kajal-Yadav31/SocialChatApp/assets/129850619/a59471d1-534f-4c11-95e9-2aad18307128)

![Screenshot 2024-06-28 112030](https://github.com/Kajal-Yadav31/SocialChatApp/assets/129850619/6c4a5de6-3120-46d5-82f2-ebc340bcd395)

![Screenshot 2024-06-28 111951](https://github.com/Kajal-Yadav31/SocialChatApp/assets/129850619/bcaced76-f819-446a-a735-78904abc4faa)

![Screenshot 2024-06-28 111920](https://github.com/Kajal-Yadav31/SocialChatApp/assets/129850619/fb22f60b-ba4b-4091-96b5-67cd11ade657)

![Screenshot 2024-06-28 111856](https://github.com/Kajal-Yadav31/SocialChatApp/assets/129850619/cea0d36c-b05d-4d8d-b7c6-217d615ec014)


![Screenshot 2024-06-28 112333](https://github.com/Kajal-Yadav31/SocialChatApp/assets/129850619/72853817-8063-432e-a565-bf8021e30afa)

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
