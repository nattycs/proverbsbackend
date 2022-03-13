from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

POST_STATUS = (
    ('draft', 'Draft'),
    ('published', 'Published')
)

class Post(models.Model):
    title = models.CharField(max_length=300)
    excerpt = models.TextField(blank=True, null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.PROTECT,
                               blank=True, null=True)
    audio = models.FileField(blank=True, null=True, upload_to='audio')
    video = models.FileField(blank=True, null=True, upload_to='videos')
    status = models.CharField(max_length=50, choices=POST_STATUS,
                              default='draft')

    def __str__(self):
        return self.title
