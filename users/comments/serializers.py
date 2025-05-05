from rest_framework import serializers
from users.models import Comments, Users


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all(), required=False, allow_null=True)
    name = serializers.SerializerMethodField()
    surname = serializers.SerializerMethodField()

    class Meta:
        model = Comments
        fields = ['comment', 'rating', 'organization', 'name', 'surname', 'user']

    def get_name(self, obj):
        return obj.user.name if obj.user else obj.name

    def get_surname(self, obj):
        return obj.user.surname if obj.user else obj.surname
