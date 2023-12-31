# Generated by Django 4.2.7 on 2023-12-03 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news1', '0004_tag_article_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['title', 'date'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('Экономика', 'Economics'), ('Sc', 'Science'), ('SP', 'Sport'), ('P', 'Policy'), ('H', 'Health'), ('T', 'Travel')], max_length=20, verbose_name='Категории'),
        ),
    ]
