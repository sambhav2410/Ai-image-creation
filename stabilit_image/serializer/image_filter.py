from rest_framework import serializers


class GenerateImageFilterSerializer(serializers.Serializer):
    prompts = serializers.ListField(
        required=True,
        allow_null=False
    )
