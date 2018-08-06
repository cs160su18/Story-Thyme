# Generated by Django 2.0 on 2018-08-05 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thyme', '0002_auto_20180805_0434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeline',
            name='favorites',
        ),
        migrations.AddField(
            model_name='timeline',
            name='familyName',
            field=models.CharField(default='Default Family Name', max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='dishName',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='timepoint',
            name='author',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='thyme.FoodUser'),
        ),
        migrations.AlterField(
            model_name='timepoint',
            name='recipe',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='thyme.Recipe'),
        ),
        migrations.AlterField(
            model_name='timepoint',
            name='timeline',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='thyme.Timeline'),
        ),
    ]