# Generated by Django 3.2.5 on 2022-03-14 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_customer_type_alter_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='type',
        ),
        migrations.AddField(
            model_name='customer',
            name='mobile',
            field=models.IntegerField(default='000', max_length=11),
        ),
    ]
