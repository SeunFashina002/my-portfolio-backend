# Generated by Django 4.1.3 on 2022-11-23 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_rename_images_projects_image_projectslideshow'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectFunctionality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('images', models.ImageField(blank=True, null=True, upload_to='')),
                ('project_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.projects')),
            ],
        ),
    ]
