from rest_framework import serializers

from invoice.models import InvoiceItems, InvoiceBillSundry, Invoice


class InvoiceItemserilizers(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItems
        fields = ["id", "item_name", "quantity", "price", "amount"]

    def validate(self, data):
        if data["quantity"] <=0 or data["price"] <=0 or data["amount"] <=0:
            raise serializers.ValidationError("Price, Quantity, and Amount must be greater than zero.")
        return data


class InvoiceBillSundrySerializers(serializers.ModelSerializer):
    class Meta:
        model = InvoiceBillSundry
        fields = '__all__'


class InvoiceSerializers(serializers.ModelSerializer):
    items = InvoiceItemserilizers(many=True)
    billsundrys = InvoiceBillSundrySerializers(many=True)

    class Meta:
        model = Invoice
        fields = '__all__'

    def validate(self, data):
        total_items_amount = sum(item["quantity"] * item["price"] for item in data["items"])
        total_billsundry_amount = sum(bill["amount"] for bill in data["billsundrys"])
        total_amount = total_billsundry_amount +total_items_amount
        if data["total_amount"] != total_amount:
            raise serializers.ValidationError("total amount mismatch")
        return data

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        billsundrys_data = validated_data.pop('billsundrys')
        invoice = Invoice.objects.create(**validated_data)
        for item_data in items_data:
            InvoiceItems.objects.create(invoice=invoice, **item_data)
        for billsundry_data in billsundrys_data:
            InvoiceBillSundry.objects.create(invoice=invoice,
                                             **billsundry_data)
        invoice.save()
        return invoice

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items')
        billsundrys_data = validated_data.pop('billsundrys')
        instance.date = validated_data.get('date', instance.date)
        instance.customer_name = validated_data.get('customer_name', instance.customer_name)
        instance.billing_address = validated_data.get('billing_address', instance.billing_address)
        instance.shipping_address = validated_data.get('shipping_address', instance.shipping_address)
        instance.gstin = validated_data.get('gstin', instance.gstin)
        instance.save()

        instance.items.all().delete()
        for item_data in items_data:
            InvoiceItems.objects.create(invoice=instance, **item_data)

        instance.billsundrys.all().delete()
        for billsundry_data in billsundrys_data:
            InvoiceBillSundry.objects.create(invoice=instance,**billsundry_data)

        instance.save()
        return instance
