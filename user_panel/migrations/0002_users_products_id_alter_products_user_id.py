# Generated by Django 4.0.4 on 2022-04-17 06:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('email', models.TextField()),
                ('password', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='id',
            field=models.BigAutoField(default=django.utils.timezone.now, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='products',
            name='user_id',
            field=models.BigIntegerField(),
        ),
    ]