from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class AppUserManager(BaseUserManager):
    def create_user(self, email, username, image, password, role='user'):
        """
        Creates and saves a User with the given email and password.
        """

        if not email:
            raise ValueError('Users must have an email address')

        if not email:
            raise ValueError('Users must have an password')

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

    def variables_class(self):
        self.OWNER = 'owner'
        self.ADMIN = 'admin'
        self.MODER = 'moderator'
        self.USER = 'user'
        self.GUEST = 'guest'

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    username = models.CharField(max_length=35)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    staff = models.BooleanField(default=False)
    image = models.ImageField(upload_to=image_path)

    objects = AppUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username', 'email', 'image', 'password']

    def get_username(self):
        return self.username

    def __str__(self):
        """
        Short about the model
        """
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin or self.is_owner or self.is_moder

    def _user_role_is(self, role):
        """
        Check if current user role matches to given.
        @:param role: user role.
        @:type role: int.
        @:rtype bool.
        @:return True if user matches given role. Else returns false.
        """
        if self.role == role:
            return True
        else:
            return False

    def is_owner(self):
        """
        Check is user is owner.
        """
        return self._user_role_is(self.OWNER)

    def is_admin(self):
        """
        Check is user is admin.
        """
        return self._user_role_is(self.ADMIN)

    def is_moder(self):
        """
        Check is user is moder.
        """
        return self._user_role_is(self.MODER)

    def is_user(self):
        """
        Check is user is user.
        """
        return self._user_role_is(self.USER)

    def is_guest(self):
        """
        Check is user is guest.
        """
        return self._user_role_is(self.GUEST)


class Meta(AbstractBaseUser.Meta):
    swappable = 'AUTH_USER_MODEL'
    verbose_name = 'Пользователь'
    verbose_name_plural = 'Пользователи'


def image_path(instance, filename):
    """
    Change path to saved user images
    """
    return '/'.join(['media', str(instance.user_owner.pk), filename])
