from django.db import models
from swampdragon.models import SelfPublishModel
from chat.serializers import MessageSerializer


class Channel(models.Model):

    title       = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    created     = models.DateTimeField(auto_now_add=True)
    modified    = models.DateTimeField(auto_now=True)
    moderator   = models.ForeignKey('auth.User', null=True, blank=True, default=None,
                                    on_delete=models.SET_NULL)


class Message(SelfPublishModel, models.Model):

    serializer_class = MessageSerializer

    user        = models.ForeignKey('auth.User')
    message     = models.TextField()
    timestamp   = models.DateTimeField(auto_now_add=True)
    modified    = models.DateTimeField(auto_now=True)
    channel     = models.ForeignKey('chat.Channel')
