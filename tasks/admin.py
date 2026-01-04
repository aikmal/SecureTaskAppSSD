from django.contrib import admin
from .models import Task, AuditLog

# This makes the Task table visible in the Admin Panel
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('title', 'user__username')

# This makes the Audit Log visible (Requirement: Admin Only)
@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('action', 'performed_by', 'timestamp')
    readonly_fields = ('action', 'performed_by', 'timestamp', 'details')