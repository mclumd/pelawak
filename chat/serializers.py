from swampdragon.serializers.model_serializer import ModelSerializer



class MessageSerializer(ModelSerializer):

    timestamp_format = "%Y-%m-%dT%H:%M:%S.%fZ"

    class Meta:
        model = "chat.Message"
        publish_fields = ('user', 'message', 'timestamp', 'channel')
        update_fields = ('message', )

    def serialize_user(self, obj):
        return obj.user.username

    def serialize_timestamp(self, obj):
        return obj.timestamp.strftime(self.timestamp_format)

    def serialize_channel(self, obj):
        return unicode(obj.channel)
