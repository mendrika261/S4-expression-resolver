# Generated by Django 4.2 on 2023-05-12 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('number', '0004_alter_character_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
