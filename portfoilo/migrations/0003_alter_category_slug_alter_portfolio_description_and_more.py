# Generated by Django 4.2.3 on 2023-08-06 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfoilo', '0002_remove_resume_description_details_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
