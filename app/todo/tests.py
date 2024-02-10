from django.test import TestCase
from .models import Task

class TaskModelTest(TestCase):

    def test_task_status_choices(self):
        task = Task(status=Task.IN_PROGRESS)
        self.assertEqual(task.get_status_display(), 'In Progress')

    def test_task_urgency_choices(self):
        task = Task(urgency=Task.HIGH)
        self.assertEqual(task.get_urgency_display(), 'High')

    def test_task_str_representation(self):
        task = Task(task="Sample Task")
        self.assertEqual(str(task), "Sample Task")

    def test_task_default_values(self):
        task = Task(task="Default Values Test")
        self.assertEqual(task.status, Task.TODO)
        self.assertEqual(task.urgency, Task.LOW)
        self.assertEqual(task.expected_time, 0)

    def test_task_deadline_nullability(self):
        task = Task(task="Deadline Test")
        self.assertIsNone(task.deadline)  # By default, deadline should be None

    def test_task_expected_time(self):
        expected_time = 45  # arbitrary number of minutes
        task = Task(task="Expected Time Test", expected_time=expected_time)
        self.assertEqual(task.expected_time, expected_time)
