# Generated by Django 3.2.13 on 2022-11-22 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
        ('accounts', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='like_movies',
            field=models.ManyToManyField(related_name='movie_like_users', to='movies.Movie'),
        ),
        migrations.AddField(
            model_name='user',
            name='like_reviews',
            field=models.ManyToManyField(related_name='review_like_users', to='movies.Review'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
