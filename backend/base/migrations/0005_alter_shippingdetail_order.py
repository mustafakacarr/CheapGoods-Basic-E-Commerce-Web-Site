# Generated by Django 4.2.1 on 2023-06-05 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_shippingdetail_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingdetail',
            name='order',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shipping_detail', to='base.order'),
        ),
    ]
