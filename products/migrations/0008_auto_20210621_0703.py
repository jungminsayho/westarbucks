# Generated by Django 3.2.4 on 2021-06-21 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_rename_menu_id_category_menu'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allergyproducts',
            old_name='allergy_id',
            new_name='allergy',
        ),
        migrations.RenameField(
            model_name='allergyproducts',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='nutrition_id',
            new_name='nutrition',
        ),
    ]
