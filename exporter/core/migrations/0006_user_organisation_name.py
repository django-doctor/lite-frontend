# Generated by Django 2.2.4 on 2019-11-21 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_auto_20190829_1255"),
    ]

    operations = [
        migrations.AddField(
            model_name="user", name="organisation_name", field=models.TextField(blank=True, default=None, null=True),
        ),
    ]