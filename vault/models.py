from django.db import models
from django.contrib.auth.models import User

class PasswordEntry(models.Model):
    CATEGORY_CHOICES = [
        ('social', 'Social'),
        ('banking', 'Banking'),
        ('work', 'Work'),
        ('shopping', 'Shopping'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    website = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.website} ({self.user.username})"

    class Meta:
        unique_together = ('user', 'website')
        ordering = ['website']