from rest_framework import serializers

class LEDControlSerializer(serializers.Serializer):
    color = serializers.CharField(max_length=7, required=False)  # expects color as hex code
    brightness = serializers.FloatField(min_value=0.0, max_value=1.0, required=False)
