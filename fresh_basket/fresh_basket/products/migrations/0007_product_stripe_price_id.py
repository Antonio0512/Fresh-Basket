# Generated by Django 4.2.3 on 2023-07-31 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stripe_price_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
