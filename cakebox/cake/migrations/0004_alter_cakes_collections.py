# Generated by Django 4.2.7 on 2023-11-14 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0003_rename_brand_cakes_flavours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cakes',
            name='collections',
            field=models.CharField(choices=[('cream cake', 'cream cake'), ('milk cake', 'milk cake'), ('cheese cake', 'cheese cake'), ('cup cake', 'cup cake'), ('plum cake', 'plum cake')], default='choclate cake', max_length=200),
        ),
    ]