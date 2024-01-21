from django.db import models

class Task(models.Model):
    TODO = 'TD'
    IN_PROGRESS = 'IP'
    DONE = 'DN'
    STATUS_CHOICES = [
        (TODO, 'To Do'),
        (IN_PROGRESS, 'In Progress'),
        (DONE, 'Done'),
    ]

    task = models.CharField(max_length=200)
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=TODO,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task
