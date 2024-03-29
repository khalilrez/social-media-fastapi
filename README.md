# FastAPI CRUD API
------- Planning to add more advanced features -------

This is a simple CRUD API built with the FastAPI framework that allows you to manage posts, users, and comments. It provides endpoints for creating, retrieving, updating, and deleting data.

## Features

- Create, retrieve, update, and delete posts
- Create and retrieve comments on posts
- User registration and login
- Authentication using JWT tokens
- Get current user information

## Installation

1. Clone the repository.

2. Install the dependencies listed in the requirements.txt file.

3. Set up the database by updating the database configuration in the `database.py` file. Run the necessary migrations to create the required tables.

4. Start the server and make sure it is running on `http://localhost:8000`.

## API Endpoints

The following API endpoints are available:

- **POSTS**
  - `POST /post`: Create a new post.
  - `GET /posts`: Retrieve all posts.
  - `GET /posts/{post_id}`: Retrieve a specific post with comments.

- **USERS**
  - `POST /token`: Login and obtain an access token.
  - `POST /register`: Register a new user.
  - `GET /users/me`: Retrieve current user information.

- **COMMENTS**
  - `POST /comment`: Create a new comment on a post.
  - `GET /post/{post_id}/comments`: Retrieve comments for a specific post.

## Authentication

To access protected endpoints, include an `Authorization` header with the value `Bearer <access_token>`. Obtain the access token by logging in (`POST /token`) with valid credentials.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
