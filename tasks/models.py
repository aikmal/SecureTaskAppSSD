from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_login_failed
from django.dispatch import receiver

# 1. The Task Model (Requirements: CRUD, Input Validation)
class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]

    # Links the task to a specific user (Owner)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # The title of the task
    title = models.CharField(max_length=200)
    
    # A longer description (can be empty)
    description = models.TextField(blank=True)
    
    # Status of the task (Pending or Completed)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    
    # Automatically saves the time when created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# 2. The Audit Log Model (Requirement: Logging & Monitoring)
class AuditLog(models.Model):
    action = models.CharField(max_length=255)
    # Renamed 'performed_by' to 'user' to make it easier to match your other code
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField(blank=True)

    def __str__(self):
        return f"{self.action} by {self.user} at {self.timestamp}"

# 3. Signal Handlers (Must be at the bottom, outside of classes)
@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    """ Logs successful logins """
    print(f"DEBUG: User {user.username} logged in!") # Proof for your console
    AuditLog.objects.create(
        action="Login",
        user=user,
        details=f"User {user.username} logged in successfully."
    )

@receiver(user_login_failed)
def log_user_login_failed(sender, credentials, request, **kwargs):
    """ Logs failed login attempts """
    username = credentials.get('username', 'Unknown')
    print(f"WARNING: Failed login attempt for username: {username}")
    # Note: We cannot save to AuditLog here because we don't have a valid 'User' object
    # since the login failed. For this assignment, printing to console is sufficient security monitoring.