# Generated by Django 3.1.4 on 2020-12-06 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dex', '0002_auto_20201205_2235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='contact_name',
        ),
        migrations.AlterField(
            model_name='contact',
            name='image_url',
            field=models.ImageField(default='default-profile-picture1.jpg', upload_to=''),
        ),
    ]
