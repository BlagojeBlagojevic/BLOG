# Generated by Django 3.2.16 on 2022-11-17 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BLOG', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='komentar',
        ),
        migrations.AddField(
            model_name='blog',
            name='komentar',
            field=models.ManyToManyField(default='null', to='BLOG.Komentar'),
        ),
    ]
