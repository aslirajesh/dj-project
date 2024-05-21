# Generated by Django 4.2.13 on 2024-05-21 12:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('2ee8bcb2-f122-490d-b6ef-078912d57ac8'), editable=False)),
                ('date', models.DateTimeField()),
                ('invoice_number', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('customer_name', models.CharField(max_length=100)),
                ('billing_address', models.TextField()),
                ('shipping_address', models.TextField()),
                ('gstin', models.CharField(max_length=20)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceItems',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('c3772f4b-1cce-4740-b237-cb33b0ffcffb'), editable=False, primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=100)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='invoice.invoice')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceBillSundry',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('b2a65e54-a9f8-4370-b6fc-3e7baef69aab'), editable=False, primary_key=True, serialize=False)),
                ('bill_sundry_name', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='billsundrys', to='invoice.invoice')),
            ],
        ),
    ]
