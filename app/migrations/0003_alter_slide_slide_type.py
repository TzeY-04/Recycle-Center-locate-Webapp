# Generated by Django 4.1.4 on 2025-05-30 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_slide_slide_type_slidecomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='slide_type',
            field=models.CharField(choices=[('paper', 'paper'), ('plastic', 'plastic'), ('can', 'can'), ('tin', 'tin')], max_length=20),
        ),
    ]
