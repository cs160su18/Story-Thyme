# Generated by Django 2.0 on 2018-08-04 20:51

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
            name='Family',
            fields=[
                ('surname', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='FoodUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thyme.Family')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('recipeName', models.TextField(max_length=30, primary_key=True, serialize=False)),
                ('ingredients', models.TextField()),
                ('directions', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('dishName', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thyme.Family')),
                ('favorites', models.ManyToManyField(to='thyme.FoodUser')),
            ],
        ),
        migrations.CreateModel(
            name='Timepoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('story', models.TextField()),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='thyme.FoodUser')),
                ('recipe', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='thyme.Recipe')),
                ('timeline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thyme.Timeline')),
            ],
        ),
    ]
