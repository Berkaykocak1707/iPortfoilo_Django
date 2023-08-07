from django.db import models
from django.utils import timezone
import os
from uuid import uuid4
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.dispatch import receiver
from django.db.models.signals import pre_save

def path_and_rename(instance, filename):
    upload_to = 'photos'
    if isinstance(instance, Profile):
        upload_to = 'photos/profile'
    elif isinstance(instance, Portfolio):
        upload_to = 'photos/portfolio/main'
    elif isinstance(instance, PortfolioPhoto):
        upload_to = 'photos/portfolio'
    ext = filename.split('.')[-1]
    # set filename as random string
    filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

class Profile(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to=path_and_rename)
    website = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=255)
    freelance = models.BooleanField(default=False)
    degree = models.CharField(max_length=255)
    email = models.EmailField()
    birthday = models.DateField()
    description = RichTextField()

    def save(self, *args, **kwargs):
        self.pk = 1
        super(Profile, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class Resume(models.Model):
    RESUME_TYPES = [
        ('EDU', 'Education'),
        ('EXP', 'Professional Experience'),
    ]
    resume_type = models.CharField(max_length=3, choices=RESUME_TYPES)
    name = models.CharField(max_length=255)
    years = models.CharField(max_length=255)
    description = RichTextField()

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name  
      
@receiver(pre_save, sender=Category)
def create_category_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)

class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    client = models.CharField(max_length=255)
    date = models.DateField(default=timezone.now)
    slug = models.SlugField(blank=True, null=True)
    address = models.CharField(max_length=255)
    photo = models.ImageField(upload_to=path_and_rename)
    description = models.TextField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

@receiver(pre_save, sender=Portfolio)
def create_portfolio_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
    
class PortfolioPhoto(models.Model):
    portfolio = models.ForeignKey(Portfolio, related_name='photos', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=path_and_rename)
