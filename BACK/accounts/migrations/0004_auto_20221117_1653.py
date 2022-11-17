# Generated by Django 3.2.13 on 2022-11-17 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_review'),
        ('accounts', '0003_auto_20221117_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='like_movies',
            field=models.ManyToManyField(related_name='movie_like_users', to='movies.Movie'),
        ),
        migrations.AlterField(
            model_name='user',
            name='like_reviews',
            field=models.ManyToManyField(related_name='review_like_users', to='movies.Review'),
        ),
    ]
