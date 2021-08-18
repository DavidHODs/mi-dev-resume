# Generated by Django 3.1.7 on 2021-08-18 02:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]