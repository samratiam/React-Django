# Generated by Django 3.0.8 on 2021-11-25 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
