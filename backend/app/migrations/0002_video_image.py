# Generated by Django 3.1.1 on 2020-09-24 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
