from django.contrib import admin
from core.models.badges import Badge, Achievement

@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('badge_name', 'badge_description')
    
@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('user', 'badge', 'date_achieved')