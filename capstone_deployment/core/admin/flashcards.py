from django.contrib import admin
from core.models.flashcards import UserFlashCards

@admin.register(UserFlashCards)
class UserFlashCardsAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('noteID', 'frontCardText', 'backCardText')
    