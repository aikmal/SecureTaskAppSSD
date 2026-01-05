from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Task, AuditLog

# 1. The Home Page (Redirects to login or dashboard)
def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return redirect('login')

# 2. Registration View (Req: User Registration)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now login.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# 3. Dashboard View (Req: RBAC - Only show user's own tasks)
@login_required # <--- Security Control: Authentication Check
def dashboard(request):
    # Security: Filter tasks so user ONLY sees their own (No IDOR)
    tasks = Task.objects.filter(user=request.user) 
    return render(request, 'dashboard.html', {'tasks': tasks})

# 4. Create Task View
@login_required
def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title: # Input Validation: Ensure title is not empty
            # Create task linked to current user
            Task.objects.create(user=request.user, title=title)
            
            # Security: Log this action (Req: Logging)
            AuditLog.objects.create(
                action="Created Task", 
                user=request.user, 
                details=f"Task '{title}' created"
            )
            return redirect('dashboard')
    return render(request, 'create_task.html')

# 5. Delete Task View
@login_required
def delete_task(request, task_id):
    # Security: Ensure user can only delete THEIR OWN task (Prevents IDOR)
    try:
        task = Task.objects.get(id=task_id, user=request.user)
        task.delete()
    except Task.DoesNotExist:
        messages.error(request, "You do not have permission to delete this task.")
    
    return redirect('dashboard')