from io import open_code
from django.db.models.fields.related import ForeignKey
import conversations
from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampedModel):

    """ Conversations Model Definition """

    participants = models.ManyToManyField('users.User', blank=True)

    def __str__(self):
        return str(self.created)


class Message(core_models.TimeStampedModel):

    message = models.TextField()
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    conversations = models.ForeignKey('conversation', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} says: {self.text}'