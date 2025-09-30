from django.contrib import admin
from polls.models import (
    Question,
    FlightLeg,
    Flight,
    Choice,
    QuestionData,
    Publication,
    Article,
)


# Register your models here.
admin.site.register(Question)
admin.site.register(Flight)
admin.site.register(FlightLeg)
admin.site.register(Choice)
admin.site.register(QuestionData)
admin.site.register(Publication)
admin.site.register(Article)
