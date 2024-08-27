## API for social networking application using Django Rest Framework #

### Follow these steps to get the application running in your local/test environment:


## Requirements ##
# Python 3.8.10

## Database ##
# SQLite3

## Run project by the following commands ##
- sudo docker-compose build
- docker-compose up

## Endpoints #

## Below are the API endpoints available in this application:

## 1. User Signup
## Method: POST
- URL: http://localhost:8000/user-signup/
## Description: Endpoint to create a new user.

## 2. User Login
## Method: POST
- URL: http://localhost:8000/login/
## Description: Endpoint for user authentication and login.

## 3. Search Users
## Method: GET
- URL: http://localhost:8000/search-users/
## Description: Endpoint to search for users.

## 4. Friend List
## Method: GET
- URL: http://localhost:8000/friend-list
## Description: Endpoint to retrieve the list of friends.

## 5. Send Friend Request
## Method: POST
- URL: http://localhost:8000/friend-request/
## Description: Endpoint to send a friend request.

## 6. Accept/Reject Friend Request
## Method: PATCH
- URL: http://localhost:8000/update-request/2/
## Description: Endpoint to accept or reject a friend request.

## 7. Pending Friend Requests
## Method: GET
- URL: http://localhost:8000/friend-request/
## Description: Endpoint to retrieve all pending friend requests.

## Postman Collection ##
## As per your requirement, I've added a Postman collection for you.
## Please find it with the name SocialAppUrls.postman_collection.json.
