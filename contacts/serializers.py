from rest_framework import serializers
from .models import Contact, PhoneNumber

class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ['id', 'number']

    def validate_number(self, value):
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError('Phone number must be exactly 10 digits.')
        return value

class ContactSerializer(serializers.ModelSerializer):
    phone_numbers = PhoneNumberSerializer(many=True)

    class Meta:
        model = Contact
        fields = ['id', 'first_name', 'last_name', 'address', 'company', 'phone_numbers']

    def validate_phone_numbers(self, value):
        if not value:
            raise serializers.ValidationError('At least one phone number is required.')
        return value

    def create(self, validated_data):
        phone_numbers_data = validated_data.pop('phone_numbers')
        contact = Contact.objects.create(**validated_data)
        for phone_number_data in phone_numbers_data:
            PhoneNumber.objects.create(contact=contact, **phone_number_data)
        return contact

    def update(self, instance, validated_data):
        phone_numbers_data = validated_data.pop('phone_numbers')
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.address = validated_data.get('address', instance.address)
        instance.company = validated_data.get('company', instance.company)
        instance.save()

        # Update phone numbers
        instance.phone_numbers.all().delete()
        for phone_number_data in phone_numbers_data:
            PhoneNumber.objects.create(contact=instance, **phone_number_data)

        return instance
