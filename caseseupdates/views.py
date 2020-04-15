from django.views import generic
from .models import Case
from django.db.models import Sum
class CaseList(generic.ListView):
    template_name='caseseupdates/caseupdate.html'


