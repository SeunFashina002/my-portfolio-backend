# Generated by Django 4.0.5 on 2022-11-26 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_projectfunctionality'),
    ]

    operations = [
        migrations.AddField(
            model_name='stack',
            name='alt',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
