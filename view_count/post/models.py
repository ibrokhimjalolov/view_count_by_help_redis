from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    view_count = models.PositiveBigIntegerField(default=0, editable=False)

    def __str__(self):
        return self.title
