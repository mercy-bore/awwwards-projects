# Generated by Django 4.0.3 on 2022-04-09 13:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('awards', '0005_awwwardprojects'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='content',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=0),
        ),
        migrations.AddField(
            model_name='rating',
            name='content_average',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='rating',
            name='design',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=0),
        ),
        migrations.AddField(
            model_name='rating',
            name='design_average',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='rating',
            name='usability',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=0),
        ),
        migrations.AddField(
            model_name='rating',
            name='usability_average',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rater', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rating',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='awards.post'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='score',
            field=models.FloatField(blank=True, default=0),
        ),
    ]