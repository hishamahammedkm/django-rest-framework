from rest_framework import serializers
from .models import Article
class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id','title','author']
# for all filed fields = '__all__'