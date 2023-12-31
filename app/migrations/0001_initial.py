# Generated by Django 3.2.23 on 2023-11-07 11:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('authors', models.JSONField()),
                ('thumbnail', models.URLField(blank=True, max_length=300)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('memo', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('record', 'Record'), ('favorite', 'Favorite'), ('delete', 'Delete')], max_length=10)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
