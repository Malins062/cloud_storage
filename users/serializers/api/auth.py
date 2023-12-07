from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ParseError

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, allow_blank=True, allow_null=True)
    email = serializers.EmailField(
        required=True,
        help_text='Адрес электронной почты',
    )
    first_name = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'password',
        )

    @staticmethod
    def validate_email(value):
        email = value.lower()
        if User.objects.filter(email=email).exists():
            raise ParseError(
                {'email': [f'Пользователь с адресом электронной почты: {email} - уже зарегистрирован.']}
            )
        return email

    @staticmethod
    def validate_phone_number(value):
        if User.objects.filter(phone_number=value).exists():
            raise ParseError(
                {'phone_number': [f'Пользователь с телефоном: {value} - уже зарегистрирован.']}
            )
        return value

    @staticmethod
    def validate_password(value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = (
            'old_password',
            'new_password',
        )

    def validate(self, attrs):
        user = self.instance
        password = attrs.pop('old_password') if 'old_password' in attrs else None
        if not user.check_password(password):
            raise ParseError(
                {'password': ['Проверьте правильность текущего пароля.']}
            )
        return attrs

    @staticmethod
    def validate_new_password(value):
        validate_password(value)
        return value

    def update(self, instance, validated_data):
        password = validated_data.pop('new_password') if 'new_password' in validated_data else None
        instance.set_password(password)
        instance.save()
        return instance


class ProfileListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class ProfileUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
