# Generated by Django 4.2.8 on 2023-12-19 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_rename_name_genre_genre_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('book', models.ManyToManyField(help_text='Books in collection', to='catalog.book')),
            ],
        ),
    ]
