from core.admin.notes import UserNotesAdmin
from core.admin.pomodoro import PomodoroAdmin
from core.admin.flashcards import UserFlashCardsAdmin
from core.admin.quiz import (UserTestAdmin, TestQuestionAdmin, TestChoicesAdmin, ChoiceAnswerAdmin)
from core.admin.badges import (BadgeAdmin, AchievementAdmin)

__all__ = [
    UserNotesAdmin,
    PomodoroAdmin,
    UserFlashCardsAdmin,
    UserTestAdmin,
    TestQuestionAdmin,
    TestChoicesAdmin,
    ChoiceAnswerAdmin,
    BadgeAdmin,
    AchievementAdmin
]