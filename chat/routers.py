from swampdragon import route_handler
from swampdragon.route_handler import ModelRouter

from chat.models import Message, Channel
from django.contrib.auth.models import User
from chat.serializers import MessageSerializer


class MessageRouter(ModelRouter):

    route_name = 'chat-route'
    serializer_class = MessageSerializer
    model = Message
    valid_verbs = ModelRouter.valid_verbs + ['chat']

    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['id'])

    def get_query_set(self, **kwargs):
        return self.model.objects.filter(channel__id=kwargs['channel_id'])

    def create(self, **kwargs):
        """
        Override the create chat for chat specific creation
        """
        errors = {}

        if 'user' not in kwargs or not kwargs['user']:
            errors['user'] = 'must supply a username'

        if 'message' not in kwargs or not kwargs['message']:
            errors['message'] =  'must supply a chat message!'

        if errors:
            self.on_error(errors)
            return

        kwargs['user'] = User.objects.filter(username=kwargs.pop('user')).first()
        if not kwargs['user']:
            errors['user'] = 'could not find a user with the supplied username'

        kwargs['channel'] = Channel.objects.first()
        if not kwargs['channel']:
            errors['channel'] = 'could not find a channel to create chat in'

        if errors:
            self.on_error(errors)
            return

        message = Message.objects.create(**kwargs)
        self.serializer = self.serializer_class(instance=message)
        self.created(message, **kwargs)






## Register models
route_handler.register(MessageRouter)
