# Generated by Django 3.1.2 on 2021-02-10 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Barbiton Torres', max_length=250),
        ),
    ]
