# Generated by Django 4.2.6 on 2023-10-16 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='additional_info',
            field=models.TextField(default='Default additional info'),
        ),
    ]