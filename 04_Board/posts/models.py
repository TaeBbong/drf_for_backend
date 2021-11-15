from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from users.models import Profile


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='author')
    profile = models.ForeignKey(Profile,
                                on_delete=models.CASCADE,
                                blank=True,
                                related_name='author_profile')
    title = models.CharField(max_length=128)
    category = models.CharField(max_length=128)
    body = models.TextField()
    image = models.ImageField(upload_to='post/', default='default.png')
    likes = models.ManyToManyField(User, related_name='like_posts')
    published_date = models.DateTimeField(default=timezone.now)

    def like_count():
        return self.likes.count()


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,
                             related_name='comments',
                             on_delete=models.CASCADE)
    text = models.TextField()
