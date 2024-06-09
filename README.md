# django-simple-auth

# User Registration
- Description: This endpoint is used to register a new user.
- URL: "http://127.0.0.1:8000/api/auth/registration/"
- Method: POST
## Request
- Headers: 
    - Content-Type: application/json
- Body(raw JSON):
    {
        "username": "your_username",
        "password1": "your_password",
        "password2": "your_password",
        "email": "your_email@example.com"
    }
## Response
- Success (HTTP 201 Created):
    - Body: 
    {
        "key": "<authentication_token>"
    }
    - Description: Returns an authentication token for the newly registered user.
- Failure (HTTP 400 Bad Request):
    - Body: 
    {
        "username": ["This field may not be blank."],
        "password1": ["This password is too short. It must contain at least 8 characters."],
        "password2": ["The two password fields didn’t match."],
        "email": ["Enter a valid email address."]
    }
    - Description: Returns an error message indicating what went wrong with the registration attempt.
#
# User Login
- URL: "http://127.0.0.1:8000/api/auth/login/"
- Method: POST
- Description: This endpoint is used to authenticate a user.
## Request
- Headers:
    - Content-Type: application/json
- Body (raw JSON):
    {
    "username": "<your_username>",
    "password": "<your_password>"
    }
## Response
- Success (HTTP 200 OK):
    - Body: 
    {
        "key": "<authentication_token>"
    }
    - Description: Returns an authentication token for the authenticated user.
- Failure (HTTP 400 Bad Request):
    - Body: 
    {
        "non_field_errors": ["Unable to log in with provided credentials."]
    }
    - Description: Returns an error message indicating what went wrong with the authentication attempt.
#
# Password Reset Request
- URL: "http://127.0.0.1:8001/api/auth/password/reset/"
- Method: POST
- Description: This endpoint is used to request a password reset. An email will be sent to the user with a link to reset their password.
## Request
- Headers:
    - Content-Type: application/json
- Body (raw JSON):
    {
    "email": "<your_email@example.com>"
    }
## Response
- Success (HTTP 200 OK):
    - Body: 
    {
        "detail": "We have sent you an email to reset your password."
    }
    - Description: Returns a success message indicating the password reset email has been sent.
- Failure (HTTP 400 Bad Request):
    - Body: 
    {
        "email": ["Enter a valid email address."]
    }
    - Description: Returns an error message indicating what went wrong with the password reset request.
#
# Password Reset Confirmation
- URL: "http://127.0.0.1:8001/api/auth/reset/confirm/<uidb64>/<token>/"
- Method: POST
- Description: This endpoint is used to confirm a password reset request.
## Request
- Headers:
    - Content-Type: application/json
- Body (raw JSON):
    {
    "uid": "UID_FROM_EMAIL",
    "token": "TOKEN_FROM_EMAIL",
    "new_password1": "new_password",
    "new_password2": "new_password"
    }
## Response
- Success (HTTP 200 OK):
    - Body: 
    {
        "detail": "Password has been reset with the new password."
    }
    - Description: Returns a success message indicating the password has been reset.

- Failure (HTTP 400 Bad Request):
    - Body: 
    {
        "new_password2": ["The two password fields didn’t match."]
    }
    - Description: Returns an error message indicating what went wrong with the password reset confirmation.
#
# User Logout
- URL: "http://127.0.0.1:8001/api/auth/logout"
- Method: POST
- Description: This endpoint is used to log out a user.
## Request
- Headers:
    - Authorization: Token <your_token>
## Response
- Success (HTTP 200 OK):
    - Body: 
    {
        "detail": "Successfully logged out."
    }
    - Description: Returns a success message indicating the user has been logged out.
#
# Get Current User Information
- URL: "http://127.0.0.1:8001/api/auth/user"
- Method: GET
- Description: This endpoint is used to retrieve the information of the currently authenticated user.
## Request
- Headers:
    - Authorization: Token <your_token>
## Response
- Success (HTTP 200 OK):
    - Body: 
    {
        "pk": <user_id>,
        "username": "<username>",
        "email": "<email>"
    }
    - Description: Returns the information of the currently authenticated user.
#
# Change Password
- URL: "http://127.0.0.1:8001/api/auth/password/change"
- Method: POST
- Description: This endpoint is used to change the password of the currently authenticated user.
## Request
- Headers:
    - Authorization: Token <your_token>
- Body (raw JSON):
    {
    "new_password1": "<new_password>",
    "new_password2": "<new_password>"
    }
## Response
- Success (HTTP 200 OK):
    - Body: 
    {
        "detail": "New password has been saved."
    }
    - Description: Returns a success message indicating the password has been changed.
- Failure (HTTP 400 Bad Request):
    - Body: 
    {
        "new_password2": ["The two password fields didn’t match."]
    }
    - Description: Returns an error message indicating what went wrong with the password change attempt.
#
# Email Verification
- URL: "http://127.0.0.1:8001/api/auth/registration/verify-email"
- Method: POST
- Description: This endpoint is used to verify the email address of a newly registered user.
## Request
- Headers:
    - Content-Type: application/json
- Body (raw JSON):
    {
    "key": "<KEY_FROM_EMAIL>"
    }
## Response
- Success (HTTP 200 OK):
    - Body: 
    {
        "detail": "Email verified."
    }
    - Description: Returns a success message indicating the email has been verified.
- Failure (HTTP 400 Bad Request):
    - Body: 
    {
        "key": ["Invalid value."]
    }
    - Description: Returns an error message indicating what went wrong with the email verification attempt.