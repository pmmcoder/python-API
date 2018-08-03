from rest_framework import serializers
from .models import Question,Choice
from django.contrib.auth.models import User

'''
version 1
'''
# class SnippetSerializer(serializers.Serializer):
    # id = serializers.IntegerField(read_only=True)
    # user_id = serializers.ReadOnlyField(source='user_id.username')
    # question_text = serializers.CharField(max_length=200)
    # pub_data = serializers.CharField(style={'base_template': 'textarea.html'})

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return Question.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.question_text = validated_data.get('question_text', instance.question_text)
    #     instance.pub_data = validated_data.get('pub_data', instance.pub_data)
    #     instance.save()
    #     return instance
'''
version 2
'''
# class SnippetSerializer(serializers.ModelSerializer):
#     user_id = serializers.ReadOnlyField(source='user_id.username')
#     class Meta:
#         model = Question
#         fields = ('id', 'user_id', 'question_text','pub_data')

'''
同上，效果一样，这是使用ModelSerializer的简单模式
'''
# class SnippetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Question
#         fields = ('id', 'question_text', 'pub_data')
# class UserSerializer(serializers.ModelSerializer):
#     snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Question.objects.all())
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'snippets')

'''
version 3
'''
# class UserSerializer(serializers.ModelSerializer):
#     snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Question.objects.all())
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'snippets')

# class SnippetSerializer(serializers.ModelSerializer):
#     user_id = serializers.ReadOnlyField(source='user_id.username')
#     class Meta:
#         model = Question
#         fields = ('id', 'user_id', 'question_text','pub_data')

# class ChoiceSerializer(serializers.ModelSerializer):
#     question_text = serializers.ReadOnlyField(source='question_id.question_text')
#     class Meta:
#         model = Choice
#         fields = ('id', 'choic_text', 'votes','question_text','question_id')

'''
vaersion 4
'''
class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Question.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.ReadOnlyField(source='user_id.username')
    class Meta:
        model = Question
        fields = ('id', 'user_id', 'question_text','pub_data')

class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    question_text = serializers.ReadOnlyField(source='question_id.question_text')
    class Meta:
        model = Choice
        fields = ('id', 'choic_text', 'votes','question_text','question_id')