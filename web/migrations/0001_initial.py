# Generated by Django 4.2.3 on 2023-08-14 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('addressid', models.IntegerField(primary_key=True, serialize=False)),
                ('addressline1', models.CharField(blank=True, max_length=60, null=True)),
                ('addressline2', models.CharField(blank=True, max_length=60, null=True)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('postalcode', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'db_table': 'address',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Creditcard',
            fields=[
                ('creditcardid', models.IntegerField(primary_key=True, serialize=False)),
                ('cardtype', models.CharField(blank=True, max_length=50, null=True)),
                ('cardnumber', models.CharField(blank=True, max_length=25, null=True)),
                ('expmonth', models.SmallIntegerField(blank=True, null=True)),
                ('expyear', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'creditcard',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customerid', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'customer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('businessentityid', models.IntegerField(primary_key=True, serialize=False)),
                ('persontype', models.CharField(blank=True, max_length=2, null=True)),
                ('namestyle', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=8, null=True)),
                ('firstname', models.CharField(blank=True, max_length=50, null=True)),
                ('middlename', models.CharField(blank=True, max_length=50, null=True)),
                ('lastname', models.CharField(blank=True, max_length=50, null=True)),
                ('suffix', models.CharField(blank=True, max_length=10, null=True)),
                ('emailpromotion', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'person',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Personcreditcard',
            fields=[
                ('personcreditcardid', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'personcreditcard',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('productnumber', models.CharField(blank=True, max_length=25, null=True)),
                ('color', models.CharField(blank=True, max_length=15, null=True)),
                ('safetystocklevel', models.SmallIntegerField(blank=True, null=True)),
                ('reorderpoint', models.SmallIntegerField(blank=True, null=True)),
                ('standardcost', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('listprice', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('size', models.CharField(blank=True, max_length=5, null=True)),
                ('sizeunitmeasurecode', models.CharField(blank=True, max_length=3, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('daystomanufacture', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Productcategory',
            fields=[
                ('productcategoryid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'productcategory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Productsubcategory',
            fields=[
                ('productsubcategoryid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'productsubcategory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Salesorderdetails',
            fields=[
                ('salesorderdetailid', models.IntegerField(primary_key=True, serialize=False)),
                ('carriertrackingnumber', models.CharField(blank=True, max_length=25, null=True)),
                ('orderqty', models.SmallIntegerField(blank=True, null=True)),
                ('specialofferid', models.IntegerField(blank=True, null=True)),
                ('unitprice', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('unitpricediscount', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'salesorderdetails',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Salesorderheader',
            fields=[
                ('salesorderid', models.IntegerField(primary_key=True, serialize=False)),
                ('revisionnumber', models.SmallIntegerField(blank=True, null=True)),
                ('orderdate', models.DateTimeField(blank=True, null=True)),
                ('duedate', models.DateTimeField(blank=True, null=True)),
                ('shipdate', models.DateTimeField(blank=True, null=True)),
                ('status', models.SmallIntegerField(blank=True, null=True)),
                ('onlineorderflag', models.BooleanField(blank=True, null=True)),
                ('purchaseordernumber', models.CharField(blank=True, max_length=25, null=True)),
                ('accountnumber', models.CharField(blank=True, max_length=15, null=True)),
                ('customerid', models.IntegerField(blank=True, null=True)),
                ('subtotal', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('taxamt', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('freight', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('totaldue', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('comment', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'db_table': 'salesorderheader',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Salesterritory',
            fields=[
                ('territoryid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('countryregioncode', models.CharField(blank=True, max_length=3, null=True)),
                ('group', models.CharField(blank=True, max_length=50, null=True)),
                ('salesytd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('saleslastyear', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('costytd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('costlastyear', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'salesterritory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('businessentityid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('salespersonid', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'store',
                'managed': False,
            },
        ),
    ]
