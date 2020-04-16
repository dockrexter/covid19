from django.views import generic
from .models import Tips

class TipsList(generic.ListView):
    queryset=(Tips.objects.filter(status=1).order_by('-created_on'))
    template_name='healthtips/healthtips.html'

class TipsDetail(generic.DetailView):
    model=Tips
    template_name='healthtips/healthtips_detail.html'