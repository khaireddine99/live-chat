# Generated by Django 4.2.1 on 2024-11-09 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_remove_post_audio_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Screenshot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='screenshots/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]