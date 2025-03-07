from django.urls import path, include
from core.views import (UserNotesListCreateView, 
                        UserNotesRetrieveUpdateDestroyView,
                        
                        PomodoroViewSet,
                        
                        UserFlashcardsListView,
                        CreateFlashcardsView, 
                        EditFlashcardView, AddFlashcardView, 
                        DeleteFlashcardView,
                        NoteFlashcardsListView,
                                   
                        UserTestListView, 
                        CreateTestView,
                        UserTestRetrieveUpdateDestroyView,
                        UserTestQuestionListView,
                        CreateTestQuestionView,
                        UserTestQuestionDetailView,
                        UserTestChoicesListView,
                        CreateQuestionChoicesView,
                        UserTestChoiceDetailView, 
                        ChoiceAnswerListView,
                        CreateChoiceAnswerView,
                        ChoiceAnswerDetailView,
                        QuestionByNoteView,
                        ChoicesByNoteView,
                        AnswerByQuestionView,
                        AnswerByNoteView,
                        
                        BadgeListCreateView,
                        AchievementsListCreateView)

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'', PomodoroViewSet, basename='pomodoro')

urlpatterns = [
    
    #UserNotes
    path('usernotes/', UserNotesListCreateView.as_view(), name='usernotes-list'),
    path('usernotes/<uuid:pk>/', UserNotesRetrieveUpdateDestroyView.as_view(), name='usernotes_detail-retrieve-update-destroy'),
    
    #Pomodoro
    path('pomodoro/', include(router.urls)),
    
    #Flashcards
    path('user-flashcards/', UserFlashcardsListView.as_view(), name='user_flashcards'),
    path('note-flashcards/<uuid:note_id>/', NoteFlashcardsListView.as_view(), name='note_flashcards'),
    path('create-flashcards/<uuid:note_id>/', CreateFlashcardsView.as_view(), name='create_flashcards'),
    path('edit-flashcard/<uuid:flashcard_id>/', EditFlashcardView.as_view(), name='edit_flashcard'),
    path('add-flashcard/<uuid:note_id>/', AddFlashcardView.as_view(), name='add_flashcard'),
    path('delete-flashcard/<uuid:flashcard_id>/', DeleteFlashcardView.as_view(), name='delete_flashcard'),
    
     # User Tests
    path('usertests/', UserTestListView.as_view(), name='usertest-list-create'),
    path('usertest-create/<uuid:note_id>/', CreateTestView.as_view(), name='usertest-create'),
    path('usertest-detail/<uuid:pk>/', UserTestRetrieveUpdateDestroyView.as_view(), name='usertest-detail'),
    
    # Test Questions
    # Use usertest/questions/0/ to show all questions
    path('usertest/questions/<uuid:note_id>/', UserTestQuestionListView.as_view(), name='user-test-questions'),
    path('questions/create/<note_id>/', CreateTestQuestionView.as_view(), name='questions-create'),
    path('question-detail/<uuid:question_id>/', UserTestQuestionDetailView.as_view(), name='question-detail'),
    
    # Question Choices
    # We can filter choices by question using the question_id, put 0 to get all choices
    # use usertest/choices/0/ to show all choices
     path('usertest/choices/<uuid:question_id>/', UserTestChoicesListView.as_view(), name='user-test-choices'),
     path('usertest/choice-create/<uuid:question_id>/', CreateQuestionChoicesView.as_view(), name='user-test-choice-create'),
     path('usertest/choice-detail/<uuid:choice_id>/', UserTestChoiceDetailView.as_view(), name='user-test-choice-detail'),
     
    # Choices Answer
    # use usertest/choice-answers/0/ to show all choices
    path('choice-answers/<uuid:choice_id>/', ChoiceAnswerListView.as_view(), name='choice-answer-list'),
    path('choice-answer/create/<uuid:choice_id>/', CreateChoiceAnswerView.as_view(), name='choice-answer-create'),
    path('choice-answer-detail/<uuid:choice_id>/', ChoiceAnswerDetailView.as_view(), name='choice-answer-detail'),
    
    #Custom Views
    path('answer-by-question/<uuid:question_id>/', AnswerByQuestionView.as_view(), name='answer-by-question'),
    path('answer-by-note/<uuid:note_id>/', AnswerByNoteView.as_view(), name='answer-by-note'),
    path('question-by-note/<uuid:note_id>/', QuestionByNoteView.as_view(), name='question-by-note'),
    path('choices-by-note/<uuid:note_id>/', ChoicesByNoteView.as_view(), name='choices-by-note'),
    
    # Badges and Achievements
    path('badges/', BadgeListCreateView.as_view(), name='badge-list-create'),
    path('achievements/', AchievementsListCreateView.as_view(), name='achievement-list-create'),
    
]
