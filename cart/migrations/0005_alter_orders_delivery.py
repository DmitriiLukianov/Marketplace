# Generated by Django 4.1.7 on 2023-03-28 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_alter_delivery_free_shipping_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='delivery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.delivery'),
        ),
    ]