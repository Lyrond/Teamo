# Generated by Django 4.0.3 on 2024-06-07 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_post_liked_by_alter_post_paragraph_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_url',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post_images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='paragraph_name',
            field=models.CharField(max_length=200),
        ),
    ]