# Generated by Django 3.1.2 on 2020-10-25 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallerymodel',
            name='kwPlace',
            field=models.DecimalField(decimal_places=3, max_digits=6, null=True),
        ),
    ]
