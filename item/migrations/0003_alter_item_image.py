# Generated by Django 5.0.6 on 2024-07-14 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, default='item/round_table.jpg', null=True, upload_to='item_images'),
        ),
    ]