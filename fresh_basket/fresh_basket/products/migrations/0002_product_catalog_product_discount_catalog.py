# Generated by Django 4.2.3 on 2023-07-07 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='catalog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='catalog.catalog'),
        ),
        migrations.AddField(
            model_name='product',
            name='discount_catalog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='discounts', to='catalog.catalog'),
        ),
    ]