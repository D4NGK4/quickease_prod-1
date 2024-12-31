from core.views.notes import UserNotesListCreateView, UserNotesRetrieveUpdateDestroyView
from core.views.pomodoro import PomodoroViewSet
from core.views.flashcards import (UserFlashcardsListView,
                                   CreateFlashcardsView, 
                                   EditFlashcardView, AddFlashcardView, 
                                   DeleteFlashcardView,
                                   NoteFlashcardsListView
                                   )
from core.views.quiz import (UserTestListView, 
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
                            AnswerByNoteView
)
from core.views.badges import BadgeListCreateView, AchievementsListCreateView

__all__ = [
    UserNotesListCreateView,
    UserNotesRetrieveUpdateDestroyView,

    PomodoroViewSet,

    UserFlashcardsListView,
    CreateFlashcardsView,
    EditFlashcardView,
    AddFlashcardView,
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
    AchievementsListCreateView
]