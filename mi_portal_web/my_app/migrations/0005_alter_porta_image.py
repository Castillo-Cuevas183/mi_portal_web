# Generated by Django 5.1.1 on 2024-09-30 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_testimonio_porta_image_porta_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='porta',
            name='image',
            field=models.ImageField(default='static/img', upload_to=''),
        ),
    ]
