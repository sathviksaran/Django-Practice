# Generated by Django 4.2.3 on 2023-08-22 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NotesApp', '0004_delete_sprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='SProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=50)),
                ('year', models.CharField(choices=[('0', 'Select Year'), ('1', '1st Year'), ('2', '2nd Year'), ('3', '3rd Year'), ('4', '4th Year')], default='0', max_length=5)),
                ('stdnt', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
