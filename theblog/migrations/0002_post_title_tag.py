# Generated by Django 3.1.2 on 2020-10-12 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default="Nil's Blog", max_length=255, null=True),
        ),
    ]
