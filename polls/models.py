import datetime
import typing

import django.utils.timezone
from django.db import models
from django.db.models.fields import NOT_PROVIDED
from django.utils.timezone import now


class Question(models.Model):

    pub_date = models.DateTimeField('date published', auto_now_add=True)
    opened = models.NullBooleanField(blank=True)

    def __set_text(self, value: str) -> None:
        self.__post_save_on_changes_data()
        self.data.text = value

    def __get_text(self) -> str:
        self.__post_save_on_changes_data()
        return self.data.text

    question_text = property(__get_text, __set_text)

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questionys'


    def __str__(self):
        return self.question_text

    def __init__(self, *args, **kwargs):
        self.__need_2_save_o2o = False
        self.__post_procedures = []
        super(Question, self).__init__(*args, **kwargs)

    def __post_save_on_changes_data(self) -> None:
        def on_save():
            """
            Executes after Question.save()
            """
            self.data.question = self
            self.data.save()
            self.__need_2_save_o2o = False

        if not hasattr(self, 'data'):
            self.data = QuestionData()

        if not self.__need_2_save_o2o:
            # Add QuestionData.save() to queue after executing Question.save()
            self._add_post_save(on_save)
            self.__need_2_save_o2o = True

    def _add_post_save(self, procedure: typing.Callable) -> None:
        """
        Add procedure to execution after Question.save()
        """
        if not callable(procedure):
            raise 'Procedure must be \"Callable\"'
        self.__post_procedures.append(procedure)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if hasattr(self, 'data'):
            self.data.save()

    def was_published_recently(self):
        return self.pub_date >= now() - datetime.timedelta(days=1)


class QuestionData(models.Model):
    text = models.CharField(max_length=200)
    question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name='data')


class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            'choice_text',
            'votes'
        )

    def __str__(self):
        return self.choice_text


class FlightLeg(models.Model):
    info = models.CharField(max_length=255, default='')
    departure = models.DateTimeField(null=True)
    arrival = models.DateTimeField(null=True)
    origin = models.CharField(max_length=3)
    destination = models.CharField(max_length=3)

    class Meta:
        unique_together = (
            'departure',
            'arrival',
            'origin',
            'destination'
        )

    def str(self):
        return f'<{self.origin} - {self.destination}: {self.departure}>'


class Flight(models.Model):
    flight_info = models.CharField(max_length=255, default='')
    flight_legs = models.ManyToManyField(FlightLeg)
    first_departure = models.DateTimeField(null=True)
    last_arrival = models.DateTimeField(null=True)
    first_origin = models.CharField(max_length=3)
    last_destination = models.CharField(max_length=3)


class Publication(models.Model):
    title = models.CharField(max_length=30)
    create_date = models.DateTimeField(null=True, blank=True, default='2000-01-01T00:00:00+00:00')

    def __init__(self, *args, **kwargs):
        constraint_fields = [field for group in self._meta.unique_together for field in group]
        for field in constraint_fields:
            try:
                val = kwargs.get(field, NOT_PROVIDED)
                default_val = self._meta.get_field(field).default
                assert val is None
                assert default_val != NOT_PROVIDED, f'{field} must have not None default value, cause it\'s constraint'
                kwargs[field] = default_val
            except:  # noqa
                pass

        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title', )
        unique_together = (
            'title',
            'create_date'
        )


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication, null=True)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline', )
