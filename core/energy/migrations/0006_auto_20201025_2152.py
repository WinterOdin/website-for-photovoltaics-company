# Generated by Django 3.1.2 on 2020-10-25 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0005_client_electricdata_electricityprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electricdata',
            name='kwp',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]