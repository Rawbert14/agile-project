from django.db import models
from django.conf import settings

class Task(models.Model):
    TODO = 'TD'
    IN_PROGRESS = 'IP'
    DONE = 'DN'
    STATUS_CHOICES = [
        (TODO, 'To Do'),
        (IN_PROGRESS, 'In Progress'),
        (DONE, 'Done'),
    ]
    
    LOW = 'L'
    MEDIUM = 'M'
    HIGH = 'H'
    URGENCY_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    ]

    task = models.CharField(max_length=200)
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=TODO,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='created_tasks',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    in_progress_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='in_progress_tasks',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    done_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='done_tasks',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='assigned_tasks',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    
    deadline = models.DateField(null=True, blank=True)
    
    urgency = models.CharField(
        max_length=1,
        choices=URGENCY_CHOICES,
        default=LOW,
    )
    

    def __str__(self):
        return self.task
