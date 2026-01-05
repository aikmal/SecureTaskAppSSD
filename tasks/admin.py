from django.contrib import admin
from .models import Task, AuditLog

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'description')

class AuditLogAdmin(admin.ModelAdmin):
    # CHANGED: 'performed_by' -> 'user'
    list_display = ('action', 'user', 'timestamp', 'details')
    # CHANGED: 'performed_by' -> 'user'
    readonly_fields = ('action', 'user', 'timestamp', 'details')
    search_fields = ('action', 'details', 'user__username')

    def has_add_permission(self, request):
        return False  # Audit logs should be read-only
    
    def has_change_permission(self, request, obj=None):
        return False  # Audit logs cannot be edited
    
    def has_delete_permission(self, request, obj=None):
        return False  # Audit logs cannot be deleted

admin.site.register(Task, TaskAdmin)
admin.site.register(AuditLog, AuditLogAdmin)