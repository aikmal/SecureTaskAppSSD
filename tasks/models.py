from django.db import models
from django.contrib.auth.models import User

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
# This meets the requirement for "Audit log page (admin only)"
class AuditLog(models.Model):
    action = models.CharField(max_length=255)
    performed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField(blank=True)

    def __str__(self):
        return f"{self.action} by {self.performed_by} at {self.timestamp}"