# Generated by Django 4.0.4 on 2022-04-17 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0002_users_products_id_alter_products_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
