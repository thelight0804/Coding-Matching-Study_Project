"""
This module defines the models for whole app uses
"""


from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    """
    This class defines the user manager for the app
    """

    def create_user(self, username: str, email: str, password: str = None) -> 'User':
        """
        This method creates a normal user
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a nickname')
        user: User = self.model(
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_admin(self, username: str, email: str, password: str = None) -> 'User':
        """
        This method creates an admin user
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a nickname')
        user: User = self.model(
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """
    This class defines the user model
    uses on Authentication
    Authorization Fields: username, password, email, social_identifier
    Authentication Fields: is_active, is_admin, is_mentor

    """
    class Gender(models.TextChoices):
        MALE = 'male', '남자'
        FEMALE = 'female', '여자'
        UNDEFINED = 'undefined', '지정 안함'

    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    social_identifier = models.CharField(max_length=150, null=True, blank=True)

    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    job = models.CharField(max_length=300, null=True, blank=True)
    # Gender : Male, Female, Undefined
    gender = models.CharField(max_length=20, choices=Gender.choices, default=Gender.UNDEFINED)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_mentor = models.BooleanField(default=False)

    # Define Const for User class
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    # define UserManager class as helper for User class
    objects = UserManager()

    # Define the stringify method
    def __str__(self):
        return self.username