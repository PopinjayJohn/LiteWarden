from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Report(models.Model)
    """Base report model used in all reports"""
    description = models.TextField(_("report description"))
    when = models.DateTimeField(_("report date and time"))
