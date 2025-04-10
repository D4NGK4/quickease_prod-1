from django.shortcuts import render
from rest_framework import viewsets
from core.models.pomodoro import Pomodoro
from core.serializers.pomodoro import PomodoroSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class PomodoroViewSet(viewsets.ModelViewSet):
    queryset = Pomodoro.objects.all()
    serializer_class = PomodoroSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Pomodoro.objects.filter(user=user)