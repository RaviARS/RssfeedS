from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


GENDER = (
    ('1', 'Male'),
    ('2', 'FeMale'),
    ('3', 'Other'),
)

ARTICLE_TYPE = (
    ('1', 'image'),
    ('2', 'video'),
    ('3', 'event'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=28, blank=True)
    permission = models.CharField(max_length=28, blank=True)
    name = models.CharField(max_length=30, blank=True)
    mobile = models.BigIntegerField(blank=True)
    email = models.EmailField(max_length=28, blank=True)
    address = models.TextField(max_length=228, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER)
    dob = models.DateField(null=True, blank=True)
    dp = models.ImageField()

    def __str__(self):
        return '%s' % self.name

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Article(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=ARTICLE_TYPE)
    caption = models.CharField(max_length=28, blank=True)
    description = models.TextField(max_length=228, blank=True)
    tags = models.CharField(max_length=228, blank=True)
    image_link = models.CharField(max_length=228, blank=True)
    video_link = models.CharField(max_length=228, blank=True)
    event_end_date = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=28, blank=True)
    created_datetime = models.DateField(null=True, blank=True)
    modified_datetime = models.DateField(null=True, blank=True)
    deleted_datetime = models.DateField(null=True, blank=True)

    def __str__(self):
        return '%s' % self.name

class Comment(models.Model):
    article = models.OneToOneField(Article, on_delete=models.CASCADE)
    comments = models.TextField(max_length=228, blank=True)
    tags = models.CharField(max_length=228, blank=True)
    image_link = models.CharField(max_length=228, blank=True)
    created_datetime = models.DateField(null=True, blank=True)
    modified_datetime = models.DateField(null=True, blank=True)
    deleted_datetime = models.DateField(null=True, blank=True)

