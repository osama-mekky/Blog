# Generated by Django 5.0 on 2023-12-26 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_post_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, default='images/post.png', null=True, upload_to=''),
        ),
    ]
