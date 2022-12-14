# Generated by Django 4.1.1 on 2022-09-12 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_coinaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coinaddress',
            name='final_balance',
            field=models.DecimalField(decimal_places=8, max_digits=24),
        ),
        migrations.AlterField(
            model_name='coinaddress',
            name='total_received',
            field=models.DecimalField(decimal_places=8, max_digits=24),
        ),
        migrations.AlterField(
            model_name='coinaddress',
            name='total_sent',
            field=models.DecimalField(decimal_places=8, max_digits=24),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(error_messages={'unique': 'A user with this email already exists.'}, help_text='The email is used as the username when signing in.', max_length=255, unique=True, verbose_name='Email'),
        ),
    ]
