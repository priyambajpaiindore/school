from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('termsAccepted',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    first_name=None
    last_name=None
    name=models.CharField(max_length=30,blank=True)
    email = models.EmailField(_('email address'), unique=True)
    city=models.CharField(max_length=30, blank=True)
    profile_pic=models.ImageField(blank=True)
    phone=models.CharField(max_length=10)
    termsAccepted=models.BooleanField()
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

class School(models.Model):
	name=models.CharField(max_length=254)
	address=models.CharField(max_length=254)

class School_Admin(models.Model):
	name=models.CharField(max_length=254)
	password=models.CharField(max_length=40)
	school=models.ForeignKey(School,on_delete=models.CASCADE)

class Teacher(models.Model):
	name=models.CharField(max_length=254)
	designation=models.CharField(max_length=254)
	selery=models.CharField(max_length=20)
	gander=models.BooleanField()
	school=models.ForeignKey(School,on_delete=models.CASCADE)

class Class(models.Model):
	standard=models.CharField(max_length=254)
	section=models.CharField(max_length=254)
	fees=models.CharField(max_length=40)

class Subject(models.Model):
	name=models.CharField(max_length=254)
	school=models.ForeignKey(School,on_delete=models.CASCADE)	

class Techersubject(models.Model):
	teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
	subject=models.ForeignKey(Subject,on_delete=models.CASCADE)

class Bus(models.Model):
	name=models.CharField(max_length=200)
	disc=models.CharField(max_length=254)
	drivername=models.CharField(max_length=254)
	number=models.CharField(max_length=254)
	contectperson=models.CharField(max_length=254)
	school=models.ForeignKey(School,on_delete=models.CASCADE)

class Parents(models.Model):
	name=models.CharField(max_length=200)
	gander=models.BooleanField()
class Student(models.Model):
	name=models.CharField(max_length=254)
	age=models.CharField(max_length=10)
	Class=models.ForeignKey(Class,on_delete=models.CASCADE)
class Result(models.Model):

	subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
	student=models.ForeignKey(Student,on_delete=models.CASCADE)
	marks=models.CharField(max_length=200)
	grad=models.CharField(max_length=20)
    
class Attendance(models.Model):
	date=models.DateField()
	attendance=models.BooleanField()
	student=models.ForeignKey(Student,on_delete=models.CASCADE)
	teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
	subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
	school=models.ForeignKey(School,on_delete=models.CASCADE)
