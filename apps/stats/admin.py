from django.contrib import admin
from .models import Injury, Competition, CompetitionYear, City, Quote, SeasonData

admin.site.register(Injury)
admin.site.register(Competition)
admin.site.register(CompetitionYear)
admin.site.register(City)
admin.site.register(Quote)
admin.site.register(SeasonData)