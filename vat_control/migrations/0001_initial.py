# Generated by Django 4.1.3 on 2023-01-18 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VAT',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=200)),
                ('customer_number', models.CharField(max_length=20)),
                ('items', models.TextField()),
                ('vat', models.TextField()),
                ('discount', models.TextField()),
                ('total_amount', models.TextField()),
            ],
        ),
    ]
