# Generated by Django 3.2.16 on 2022-11-17 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Komentar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nik', models.CharField(max_length=64)),
                ('komentar', models.CharField(max_length=64)),
                ('vrijeme_komentara', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naslov', models.CharField(max_length=64)),
                ('autor', models.CharField(max_length=64)),
                ('vrijeme_kreiranja', models.TimeField()),
                ('tekst', models.CharField(max_length=400)),
                ('komentar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BLOG.komentar')),
            ],
        ),
    ]
