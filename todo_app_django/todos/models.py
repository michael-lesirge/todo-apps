from django.db import models
from django.utils import timezone
import datetime

class TodoManager(models.Manager):
    def get_uncompleted_count(self):
        return self.model.objects.filter(completed=False).count()

class Todo(models.Model):
    name = models.CharField(max_length=24)
    info = models.TextField(blank=True)

    completed = models.BooleanField(default=False)

    complete_by_days = models.PositiveIntegerField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    objects = TodoManager()

    @property
    def should_be_completed_by(self) -> datetime.datetime:
        return self.date_created + datetime.timedelta(days=self.complete_by_days)
    
    @property
    def is_past_deadline(self) -> bool:
        return timezone.now() > self.should_be_completed_by

    def __str__(self) -> str:
        return self.name
