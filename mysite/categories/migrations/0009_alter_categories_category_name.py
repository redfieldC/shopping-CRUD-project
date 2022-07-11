# Generated by Django 4.0.5 on 2022-07-05 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_alter_products_categories_alter_products_colors_and_more'),
        ('categories', '0008_alter_categories_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='category_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.products'),
        ),
    ]
