# Generated by Django 4.2.3 on 2023-08-06 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfoilo', '0003_alter_category_slug_alter_portfolio_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='category',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='categories',
            field=models.ManyToManyField(to='portfoilo.category'),
        ),
    ]
