# SocialDj - Your Social Media Hub

## Project Demo video:

### User Authentication:

https://github.com/user-attachments/assets/86133df2-01d6-4796-8b7c-5a41a451dbd0


### Post Creation demo:

https://github.com/user-attachments/assets/be336e57-4dca-4fc1-a943-9c6e7f7aea5c


### Real-time Chat demo:

https://github.com/user-attachments/assets/181e3b63-b2a8-4f69-bed4-3b8042461f37



## ScreenShots of project:
### Registration Page:
![register](https://github.com/user-attachments/assets/90767183-a173-4d0e-bfa9-eae7150d8933)

### Login Page:
![login](https://github.com/user-attachments/assets/97bf1bfb-de96-43fb-a8b8-b8fc8b7ac46d)

### Forgot Password Page:
![forgetpassword](https://github.com/user-attachments/assets/b41d3c87-4491-497e-be1e-ee129790813f)

### Reset Password Page:
![reset password](https://github.com/user-attachments/assets/e3ed1866-cc28-435d-9343-3ca9fdda193c)

### Profile Creation Page:
![editprofile](https://github.com/user-attachments/assets/6de6c0f7-eec1-4f5a-8925-4a3c56305107)

### Profile View Page:
![profile view](https://github.com/user-attachments/assets/6f53f6e0-3bf1-4099-b233-e2da006d66df)

### Home Page :
![home page](https://github.com/user-attachments/assets/cf41ea44-6fad-49dd-87a8-8f118a07997f)

### Post creation page:
![post page](https://github.com/user-attachments/assets/556d73b7-a3fd-4a1e-ab47-f2c387e3b4dd)

### Post deletion:
![delete post](https://github.com/user-attachments/assets/d4ceda5e-bbb6-49ed-abbc-e4fc8655148d)

### Post view and comment page :
![comment](https://github.com/user-attachments/assets/688c436f-0889-46fd-b5b6-51c9b002de14)

### Comment Deletion :
![delete comment](https://github.com/user-attachments/assets/ce7a0994-6485-443f-b761-def6c2d2ae45)

### Reply Delection :
![deletereply](https://github.com/user-attachments/assets/750309f0-5ba1-44ca-bebe-70161bbc92e7)

### Chat Page :
![chat](https://github.com/user-attachments/assets/4e66c627-6bfb-4e6c-97fd-4dd0c4343ea3)







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
