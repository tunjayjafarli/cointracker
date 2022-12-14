# Generated by Django 4.1.1 on 2022-09-12 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoinAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=35, verbose_name='Address')),
                ('address_hash', models.CharField(max_length=160, verbose_name='Address Hash')),
                ('coin_name', models.CharField(blank=True, help_text='Name of the coin or blockchain', max_length=255, verbose_name='Coin Name')),
                ('total_transactions', models.IntegerField(verbose_name='Total number of transcations')),
                ('total_received', models.DecimalField(decimal_places=8, max_digits=16)),
                ('total_sent', models.DecimalField(decimal_places=8, max_digits=16)),
                ('final_balance', models.DecimalField(decimal_places=8, max_digits=16)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
            options={
                'verbose_name': 'Coin Address',
                'verbose_name_plural': 'Coin Addresses',
            },
        ),
    ]
