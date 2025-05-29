from django.db import models

# Create your models here.

class Member(models.Model):
    member_ID = models.CharField(max_length=4, primary_key=True)
    member_name = models.CharField(max_length=100)
    member_password = models.CharField(max_length=20)

class Slide(models.Model):
    SLIDE_TYPE_CHOICES = [
        ('Paper', 'Paper'),
        ('Can', 'Can'),
        ('Tin', 'Tin'),
    ]
    slide_ID = models.CharField(max_length=4, primary_key=True)
    slide_type = models.CharField(max_length=20, choices=SLIDE_TYPE_CHOICES)
    slide_title = models.TextField()
    slide_description = models.TextField()

class RecycleCenter(models.Model):
    rc_ID = models.CharField(max_length=4, primary_key=True)
    rc_address = models.CharField(max_length=100)
    rc_name = models.CharField(max_length=100)
