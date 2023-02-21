# Generated by Django 4.1.6 on 2023-02-08 14:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articleseries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(blank=True, default='', max_length=200)),
                ('slug', models.SlugField(unique=True, verbose_name='Series Slug')),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(blank=True, default='', max_length=200)),
                ('article_slug', models.SlugField(unique=True, verbose_name='Series Slug')),
                ('content', models.TextField()),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
                ('modified', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
                ('series', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='main.articleseries', verbose_name='Series')),
            ],
        ),
    ]