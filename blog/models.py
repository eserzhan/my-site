from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    cover = models.ImageField(upload_to='images/', null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Product1(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    cover = models.ImageField(upload_to='images/',  validators=[FileExtensionValidator(['jpg', 'png'])], null=True, blank=True)
    #published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Product2(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    cover = models.ImageField(upload_to='images/',  validators=[FileExtensionValidator(['jpg', 'png'])], null=True, blank=True)
    #published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Product3(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    cover = models.ImageField(upload_to='images/',  validators=[FileExtensionValidator(['jpg', 'png'])], null=True, blank=True)
    #published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Product4(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    cover = models.ImageField(upload_to='images/',  validators=[FileExtensionValidator(['jpg', 'png', 'tif'])], null=True, blank=True)
    #published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title