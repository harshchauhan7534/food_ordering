# Generated by Django 5.0.1 on 2024-02-02 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_food',
            name='numPer',
            field=models.TextField(),
        ),
    ]
