# Generated by Django 2.2.12 on 2020-04-02 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_fakestuff"),
    ]

    operations = [
        migrations.AddField(
            model_name="modelaline",
            name="something",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
