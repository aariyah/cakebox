# Generated by Django 4.2.7 on 2023-11-14 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0006_cakevarients_shape'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cakes',
            name='flavours',
            field=models.CharField(choices=[('choclate', 'choclate'), ('vanilla', 'vanilla'), ('mango', 'mango'), ('blueberry', 'blueberry'), ('pineapple', 'pineapple'), ('hazelnut', 'hazelnut'), ('almond', 'almond'), ('strawberry', 'strawberry')], default='choclate', max_length=200),
        ),
    ]
