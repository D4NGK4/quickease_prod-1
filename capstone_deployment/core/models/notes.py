from django.db import models
from utils.model import Model
from django.utils.translation import gettext_lazy as _
from core.openai_generators.text_summarizer import summarize
from users.models import User
from core.openai_generators.title_generator import generate_title
from django.db import transaction

# Create your models here.

class UserNotes(Model):
    notetitle = models.TextField(_("Note Title"), default="")
    notecontents = models.TextField(_("Note Contents"))
    notedatecreated = models.DateTimeField(auto_now_add=True)
    notesummary = models.TextField(_("Note Summary"), blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')

    class Meta:
        verbose_name = _("User Note")
        verbose_name_plural = _("User Notes")

    def save(self, *args, **kwargs):
        with transaction.atomic():
            if not self.notesummary:
                self.notesummary = summarize(
                    text=self.notecontents,
                    detail=0.9,
                    model='gpt-4o',
                    minimum_chunk_size=500,
                    summarize_recursively=True,
                    chunk_delimiter="<break>"
                )
                self.notetitle = generate_title(self.notesummary)
            super(UserNotes, self).save(*args, **kwargs)

    def __str__(self):
        return self.notetitle
