from rest_framework import serializers
from ..models import Post

class PostSerializer(serializers.ModelSerializer):
    date_created = serializers.DateTimeField(format='%-I:%M %p, %-d %b %Y')
    class Meta:
        model = Post
        fields = '__all__'
