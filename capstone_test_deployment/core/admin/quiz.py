from django.contrib import admin
from core.models.quiz import UserTest, TestQuestion, TestChoices, ChoiceAnswer

@admin.register(UserTest)
class UserTestAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('note', 'TestScore', 'TestTotalScore','TestDateCreated')
   

@admin.register(TestQuestion)
class TestQuestionAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('test', 'TestQuestion')
   

@admin.register(TestChoices)
class TestChoicesAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('question', 'item_choice_text', 'isAnswer')
   

@admin.register(ChoiceAnswer)
class ChoiceAnswerAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('answer',)