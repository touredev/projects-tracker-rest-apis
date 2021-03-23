from rest_framework import serializers

from .models import Project, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class TagRelatedField(serializers.StringRelatedField):
    def to_representation(self, value):
        return TagSerializer(value).data

    def to_internal_value(self, data):
        return data

class ProjectSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    tags = TagRelatedField(many=True, required=False)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Project
        fields = ['id', 'title', 'description', 'status', 'started_at', 'ended_at', 'created_at', 'updated_at', 'owner', 'tags']
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        tags = validated_data.pop('tags', None)
        instance = self.Meta.model(**validated_data)
        instance.save()
        instance.tags.add(*tags)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        tags = validated_data.pop('tags', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if tags is not None:
            instance.tags.clear()
            instance.tags.add(*tags)
            instance.save()
        return instance