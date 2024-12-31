from django.db import models
from utils.model import Model
from django.utils.translation import gettext_lazy as _
from core.models.notes import UserNotes

# Create your models here.
class UserFlashCards(Model):
    noteID = models.ForeignKey(UserNotes, on_delete=models.CASCADE)
    frontCardText = models.CharField(_("Front Card Text"), max_length=100, default="")
    backCardText = models.CharField(_("Back Card Text"), max_length=500, default="")
    
    class Meta: 
        verbose_name = _("User FlashCard")
        verbose_name_plural = _("User FlashCards")
    
    def __str__(self):
        return str(self.noteID) + " " + str(self.frontCardText)
        
    
    
