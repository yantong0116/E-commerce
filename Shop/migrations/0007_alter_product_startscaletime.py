# Generated by Django 3.2.5 on 2021-12-09 10:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0006_alter_product_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='startScaleTime',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
