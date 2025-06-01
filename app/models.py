from django.db import models

# Create your models here.

class Member(models.Model):
    member_ID = models.CharField(max_length=4, primary_key=True)
    member_name = models.CharField(max_length=100)
    member_password = models.CharField(max_length=20)

class Slide(models.Model):
    SLIDE_TYPE_CHOICES = [
        ('paper', 'paper'),
        ('plastic', 'plastic'),
        ('can', 'can'),
        ('tin', 'tin'),
    ]
    slide_ID = models.CharField(max_length=4, primary_key=True)
    slide_type = models.CharField(max_length=20, choices=SLIDE_TYPE_CHOICES)
    slide_title = models.TextField()
    slide_description = models.TextField()

class Region(models.Model):
    REGION_CHOICES = [
        ('puchong', 'puchong'),
        ('kajang', 'kajang'),
    ]
    region = models.CharField(max_length=100,primary_key=True,choices=REGION_CHOICES)
    region_latitude = models.FloatField()
    region_longitude = models.FloatField()

class RecycleCenter(models.Model):
    rc_ID = models.CharField(max_length=4, primary_key=True)
    rc_latitude = models.FloatField(null=True)
    rc_longitude = models.FloatField(null=True)
    rc_address = models.TextField()
    rc_name = models.CharField(max_length=100)
    rc_region = models.ForeignKey(Region, on_delete=models.CASCADE,null=True)

class SlideComment(models.Model):
    slide_ID = models.ForeignKey(Slide, on_delete=models.CASCADE)
    member_ID = models.ForeignKey(Member, on_delete=models.CASCADE,null=True)
    comment = models.TextField()

class NewFoundRecycleCenter(models.Model):
    rc_latitude = models.FloatField(null=True)
    rc_longitude = models.FloatField(null=True)
    rc_name = models.CharField(max_length=100)
    rc_address = models.TextField()
    rc_region = models.ForeignKey(Region, on_delete=models.CASCADE,null=True)