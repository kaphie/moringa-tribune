# Generated by Django 2.0.7 on 2020-05-21 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20200521_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default='default.jpg', upload_to='articles/'),
        ),
    ]
