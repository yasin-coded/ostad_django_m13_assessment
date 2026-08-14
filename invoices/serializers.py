from rest_framework import serializers
from .models import Invoice, InvoiceItem


class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = ['id', 'product', 'quantity', 'price']

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("Quantity must be greater than zero.")
        return value


class InvoiceSerializer(serializers.ModelSerializer):
    items = InvoiceItemSerializer(many=True)  # nested — accepts a LIST of items

    class Meta:
        model = Invoice
        fields = ['id', 'customer', 'created_by', 'created_at', 'items']
        read_only_fields = ['created_by', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        invoice = Invoice.objects.create(**validated_data)
        for item_data in items_data:
            InvoiceItem.objects.create(invoice=invoice, **item_data)
        return invoice