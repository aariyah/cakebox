# Generated by Django 4.2.7 on 2023-11-14 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0002_cakes_cakevarients_category_reviews_orders_offers_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cakes',
            old_name='brand',
            new_name='flavours',
        ),
    ]
