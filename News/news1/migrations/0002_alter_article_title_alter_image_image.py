# Generated by Django 4.2.7 on 2023-12-28 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(default='', max_length=150, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='article_images/'),
        ),
    ]
