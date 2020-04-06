from django.db import models
from froala_editor.fields import FroalaField

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)
class Posts(models.Model):
    title = models.CharField(max_length=220, unique=True)
    slug = models.SlugField(unique=True, max_length=220)
    description = models.CharField(max_length=220)

    body = models.TextField()

    post_date = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    objects = models.Manager()

    class Meta:
        ordering = ['-post_date']

    def __str__(self):
        return self.title
