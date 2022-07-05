# Generated by Django 4.0.6 on 2022-07-05 15:39

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
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('icon', models.ImageField(upload_to='icons/')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('social', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.social')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='link', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
