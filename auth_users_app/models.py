from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# roles: (3, 'admin'), (2, 'moderator'), (1, 'user'), (0, 'public_user')
class AppUserManager(BaseUserManager):
    def create_user(self, email, username, image, role=1, password=None):
        """
        Creates and saves a User with the given email and password.
        """

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            role=role,
            image=image
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, username):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            username,
            image='localhost:3000/static/admin.png',
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class AppUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    username = models.CharField(max_length=35)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    image = models.URLField(max_length=225)

    objects = AppUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username', 'email', 'image', 'password']

    def get_username(self):
        return self.username

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    # def has_perm(self, perm, obj=None):
    #     "Does the user have a specific permission?"
    #     # Simplest possible answer: Yes, always
    #     return True
    #
    # def has_module_perms(self, app_label):
    #     "Does the user have permissions to view the app `app_label`?"
    #     # Simplest possible answer: Yes, always
    #     return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin