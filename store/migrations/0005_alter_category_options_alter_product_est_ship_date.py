# Generated by Django 5.0.7 on 2024-07-13 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_product_stock_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='product',
            name='est_ship_date',
            field=models.DateField(choices=[('Today', 'Today'), ('3 Days After', '3 Days After'), ('7 Days After', '7 Days After')]),
        ),
    ]
