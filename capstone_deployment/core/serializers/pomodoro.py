from rest_framework import serializers
from core.models.pomodoro import Pomodoro


class PomodoroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pomodoro
        fields = '__all__'

