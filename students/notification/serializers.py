from rest_framework import serializers

from students.models import Notification
from students.models.student import Student


class NotificationSerializer(serializers.ModelSerializer):
    student_id = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), source='student', write_only=True)
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = '__all__'

    def get_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d')
