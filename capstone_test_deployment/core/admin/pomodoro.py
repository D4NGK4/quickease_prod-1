from django.contrib import admin
from core.models.pomodoro import Pomodoro

@admin.register(Pomodoro)
class PomodoroAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('user', 'study_time', 'short_break', 'long_break', 'show_timer')