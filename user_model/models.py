from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class AccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("User must have an Email Address.")
        if not username:
            raise ValueError("User must have an Username.")

        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):

        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username
        )

        user.is_admin = True
        user.is_staff = True
        user.is_doctor = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date_joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last_login', auto_now=True)
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.CharField(max_length=5)
    gender = models.CharField(max_length=10)
    mobile = models.CharField(max_length=12, null=True)
    address = models.CharField(max_length=150)
    specialization = models.CharField(max_length=30)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    objects = AccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_active

    def has_module_perms(self, app_label):
        return True
