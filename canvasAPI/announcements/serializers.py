from rest_framework import serializers

from announcements.models import Announcement

class AnnouncementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Announcement
        fields = (
            'id',
            'title',
            'body',
            'course',
        )