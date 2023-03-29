from  rest_framework import serializers
from holders.models import Holders


class HoldersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Holders
        fields = '__all__'

    def update(self, instance, validated_data):
        if instance.arrears != validated_data.get('arrears'):
            raise serializers.ValidationError('Невозможно изменить поле "задолженность перед поставщиком"')
        return super().update(instance, validated_data)
