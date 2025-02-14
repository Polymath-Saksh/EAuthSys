# EAuthSys

## Facial Recognition Module

The `facial_recognition` module provides functionality for facial recognition authentication. It includes methods for capturing and verifying facial data.

### Usage

```python
from auth.facial_recognition.facial_recognition import FacialRecognition

facial_recognition = FacialRecognition()
facial_recognition.capture_face()
is_verified = facial_recognition.verify_face()
```

## OTP Module

The `otp` module provides functionality for OTP-based authentication. It includes methods for generating and verifying OTPs.

### Usage

```python
from auth.otp.otp import OTP

otp = OTP()
generated_otp = otp.generate_otp()
is_verified = otp.verify_otp(generated_otp)
```

## Password Module

The `password` module provides functionality for password-based authentication. It includes methods for hashing and verifying passwords.

### Usage

```python
from auth.password.password import Password

password = Password()
hashed_password = password.hash_password("my_password")
is_verified = password.verify_password("my_password", hashed_password)
```

## Security Questions Module

The `security_questions` module provides functionality for security questions-based authentication. It includes methods for setting and verifying security questions.

### Usage

```python
from auth.security_questions.security_questions import SecurityQuestions

security_questions = SecurityQuestions()
security_questions.set_security_questions({"What is your pet's name?": "Fluffy"})
is_verified = security_questions.verify_answers({"What is your pet's name?": "Fluffy"})
```
