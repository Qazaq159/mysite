from django.contrib import admin
from translated_fields import TranslatedFieldAdmin
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
@admin.register(Publication)
class PublicationAdmin(TranslatedFieldAdmin, admin.ModelAdmin):
    pass
admin.site.register(Article)
