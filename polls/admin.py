from django.contrib import admin
from polls.models import Question, FlightLeg, Flight


# Register your models here.
admin.site.register(Question)
admin.site.register(Flight)
admin.site.register(FlightLeg)