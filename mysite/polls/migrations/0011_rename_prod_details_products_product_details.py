# Generated by Django 4.0.5 on 2022-07-07 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_rename_colors_products_color'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='prod_details',
            new_name='product_details',
        ),
    ]
