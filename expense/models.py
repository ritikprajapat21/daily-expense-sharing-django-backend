from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, phone_number, password = None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        
        email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, phone_number, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=254, unique=True)
    # Including country code
    phone_number = models.CharField(max_length=15)
    name = models.CharField(max_length=255)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'name']

    objects = UserManager()
    
class Expense(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenditure')
    total_amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.created_by.name}: {self.total_amount}"
    
class Split(models.Model):
    split_choices = {'EX': "Exact", 'EQ': "Equal", 'PE': "Percentage"}

    amount = models.DecimalField(decimal_places=2, max_digits=12)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="expense_split")
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, related_name="split")
    split_method = models.CharField(max_length=2, choices=split_choices, default=split_choices['EQ'])

    def __str__(self):
        return f"{self.user}: {self.amount}"