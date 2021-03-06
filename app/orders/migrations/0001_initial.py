# Generated by Django 2.0.6 on 2018-06-17 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.SmallIntegerField(db_column='orderid', primary_key=True, serialize=False)),
                ('order_date', models.DateField(blank=True, db_column='orderdate', null=True)),
                ('required_date', models.DateField(blank=True, db_column='requireddate', null=True)),
                ('shipped_date', models.DateField(blank=True, db_column='shippeddate', null=True)),
                ('freight', models.FloatField(blank=True, null=True)),
                ('ship_name', models.CharField(blank=True, db_column='shipname', max_length=40, null=True)),
                ('ship_address', models.CharField(blank=True, db_column='shipaddress', max_length=60, null=True)),
                ('ship_city', models.CharField(blank=True, db_column='shipcity', max_length=15, null=True)),
                ('ship_region', models.CharField(blank=True, db_column='shipregion', max_length=15, null=True)),
                ('ship_postalcode', models.CharField(blank=True, db_column='shippostalcode', max_length=10, null=True)),
                ('ship_country', models.CharField(blank=True, db_column='shipcountry', max_length=15, null=True)),
            ],
            options={
                'db_table': 'orders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.OneToOneField(db_column='orderid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='orders.Order')),
                ('unit_price', models.FloatField(db_column='unitprice')),
                ('quantity', models.SmallIntegerField(db_column='quantity')),
                ('discount', models.FloatField(db_column='discount')),
            ],
            options={
                'db_table': 'order_details',
                'managed': False,
            },
        ),
    ]
