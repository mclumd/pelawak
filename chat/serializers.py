from swampdragon.serializers.model_serializer import ModelSerializer

class MessageSerializer(ModelSerializer):

    class Meta:
        model = "chat.Message"
        publish_fields = ('user', 'message', 'timestamp')

    def serialize_user(self, obj):
        return obj.user.username
