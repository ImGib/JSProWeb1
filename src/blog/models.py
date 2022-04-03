from multiprocessing.spawn import import_main_path
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify


STATUS = (
    ('discussion', 'Discussion'),
    ('learning', 'Learning'),
    ('techtalk', 'Teach Talk')
)

class Post(models.Model):
    title               = models.CharField(max_length=200, unique=True)
    slug                = models.SlugField(max_length=200, unique=True)
    author              = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on          = models.DateTimeField(auto_now= True)
    created_on          = models.DateTimeField(auto_now_add=True)
    content             = models.TextField()
    status              = models.CharField(max_length=20,choices=STATUS, default='discussion')
    is_published        = models.BooleanField(default=True)
    blog_views          = models.IntegerField(default=0)
    time_start_tech     = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)