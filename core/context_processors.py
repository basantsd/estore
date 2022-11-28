from site_settings.models import SiteSetting
from datetime import date

def SiteData(request):
    site_data = SiteSetting.objects.get(id=1)
    year = date.today().year
    context = {'site_data': site_data,'year':year}
   
    return context