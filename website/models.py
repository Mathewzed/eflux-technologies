from django.db import models

class Settings(models.Model):

    whatsapp_number = models.CharField(max_length=20, blank=True, null=True)

    phone_number = models.CharField(max_length=30, blank=True, null=True)

    email = models.EmailField(blank=True, null=True)

    class Meta:

        verbose_name_plural = 'Settings'

    def save(self, *args, **kwargs):

        self.id = 1

        super().save(*args, **kwargs)

    def __str__(self):

        return 'Site Settings'


class Project(models.Model):

    title = models.CharField(max_length=200)

    image = models.ImageField(upload_to='projects/')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.title


class Contact(models.Model):

    name = models.CharField(max_length=200)

    email = models.EmailField()

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.name