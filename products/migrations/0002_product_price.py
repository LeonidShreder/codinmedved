# Generated by Django 2.1.5 on 2019-02-13 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=10),
        ),
    ]
