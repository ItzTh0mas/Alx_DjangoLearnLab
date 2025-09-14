# relationship_app/models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    """
    Custom user manager that handles user creation and queries
    for the custom user model with additional fields.
    """
    
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and return a regular user with the given email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and return a superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    """
    Custom user model extending Django's AbstractUser
    with additional fields for date of birth and profile photo.
    """
    
    # Additional custom fields
    date_of_birth = models.DateField(
        null=True, 
        blank=True, 
        help_text="Enter your date of birth"
    )
    
    profile_photo = models.ImageField(
        upload_to='profile_photos/', 
        null=True, 
        blank=True,
        help_text="Upload your profile photo"
    )
    
    # Optional: Make email required and unique
    email = models.EmailField(
        'email address', 
        unique=True,
        help_text="Enter a valid email address"
    )
    
    # Use email as the username field instead of username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    # Assign the custom manager
    objects = CustomUserManager()
    
    class Meta:# type: ignore
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'custom_user'
    
    def __str__(self):
        return f"{self.email} - {self.first_name} {self.last_name}"
    
    @property
    def age(self):
        """
        Calculate and return the user's age based on date of birth.
        """
        if self.date_of_birth:
            today = timezone.now().date()
            return today.year - self.date_of_birth.year - (# type: ignore
                (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)# type: ignore
            )
        return None
    
    def get_full_name(self):
        """
        Return the user's full name.
        """
        return f"{self.first_name} {self.last_name}".strip()
    
    def get_short_name(self):
        """
        Return the user's first name.
        """
        return self.first_name
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.name)

class Book(models.Model):
    title = models.CharField(max_length=200)
    # ForeignKey relationship: Many books can have one author
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.author.name}"

class Library(models.Model):
    name = models.CharField(max_length=100)
    # ManyToManyField relationship: A library can have many books,
    # and a book can be in many libraries
    books = models.ManyToManyField(Book)

    def __str__(self) -> str:
        return str(self.name)

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    # OneToOneField relationship: One librarian per library
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.library.name}"

# New UserProfile model
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')
    
    def __str__(self) -> str:
        return f"{self.user.username} - {self.role}"# type: ignore

# Signal to automatically create UserProfile when User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create a UserProfile when a new User is created"""
    if created:
        UserProfile.objects.create(user=instance)  # type: ignore

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Save the UserProfile when User is saved"""
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()
    else:
        UserProfile.objects.create(user=instance)  # type: ignore