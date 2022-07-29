from django.db import models
from django.utils.translation import gettext_lazy as _


class ContentType(models.IntegerChoices):
    THEORETICAL_HOMEWORK = 0, _('Theoretical Home Work')
    PRACTICAL_HOMEWORK = 1, _('Practical Home Work')
    EXAM = 2, _('Exam')
    MIDTERM = 3, _('Midterm')
    FINAL = 4, _('Final')
    HANDOUT = 5, _('Handout')
    SOURCE = 6, _('Source')
    SLIDE = 7, _('Slide')
    CLASS_VIDEO = 8, _('Class Video')
    TA_CLASS_VIDEO = 9, _('TA Class Video')
