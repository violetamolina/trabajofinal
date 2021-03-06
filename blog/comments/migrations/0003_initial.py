# Generated by Django 4.0 on 2021-12-20 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comments', '0002_initial'),
        ('users', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.profile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auth.user'),
        ),
    ]
