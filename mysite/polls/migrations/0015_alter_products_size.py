# Generated by Django 4.0.5 on 2022-07-08 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Size', '0004_alter_size_size_name'),
        ('polls', '0014_remove_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='size',
            field=models.ForeignKey(choices=[('SM', 'SM'), ('MD', 'MD'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('XXXL', 'XXXL')], on_delete=django.db.models.deletion.CASCADE, to='Size.size'),
        ),
    ]
