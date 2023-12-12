# Generated by Django 4.2.7 on 2023-11-25 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('E', 'Economics'), ('SC', 'Science'), ('SP', 'Sport'), ('P', 'Policy'), ('H', 'Health'), ('T', 'Travel')], default=0, max_length=20),
            preserve_default=False,
        ),
    ]