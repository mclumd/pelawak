from swampdragon import route_handler
from swampdragon.route_handler import ModelRouter

from chat.models import Message
from chat.serializers import MessageSerializer


class MessageRouter(ModelRouter):

    route_name = 'chat-message'
    serializer_class = MessageSerializer
    model = Message

    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['id'])

    def get_query_set(self, **kwargs):
        return self.model.objects.filter(channel__id=kwargs['channel_id'])


route_handler.register(MessageRouter)
