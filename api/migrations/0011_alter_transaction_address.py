# Generated by Django 4.1.1 on 2022-09-12 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_coinaddress_last_updated_transaction_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.coinaddress'),
        ),
    ]
