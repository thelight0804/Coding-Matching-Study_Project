# Generated by Django 4.0.4 on 2022-05-12 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='social_identifier',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
