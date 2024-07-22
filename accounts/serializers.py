from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    profile_picture = serializers.ImageField(required=False, allow_null=True)
    phone_numbers = serializers.CharField(write_only=True, required=True)  # Updated to CharField

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name', 'date_of_birth', 'gender', 'phone_numbers', 'address', 'profile_picture')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        # Validate phone numbers
        phone_numbers = attrs.get('phone_numbers', '')
        phone_numbers_list = [num.strip() for num in phone_numbers.split(',')]
        for phone_number in phone_numbers_list:
            if not phone_number.isdigit() or len(phone_number) != 10:
                raise serializers.ValidationError({"phone_numbers": "Each phone number should be 10 digits long."})

        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        phone_numbers = validated_data.pop('phone_numbers', '')
        phone_numbers_list = [num.strip() for num in phone_numbers.split(',')]

        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            date_of_birth=validated_data['date_of_birth'],
            gender=validated_data['gender'],
            phone_number=phone_numbers_list[0] if phone_numbers_list else '',  # Use the first phone number
            address=validated_data['address'],
            profile_picture=validated_data.get('profile_picture')
        )
        user.set_password(validated_data['password'])
        user.save()

        # Handle additional phone numbers if necessary
        # For simplicity, we're only saving the first phone number in this example

        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data.update({'email': self.user.email})
        return data
