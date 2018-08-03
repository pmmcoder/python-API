from django.contrib.auth.models import User
from cmdb.models import Question,Choice
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Serializers define the API representation.
class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question_text', 'pub_data')

# ViewSets define the view behavior.
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

# Serializers define the API representation.
class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'choic_text', 'votes','question_id')

# ViewSets define the view behavior.
class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

# Routers provide an easy way of automatically determining the URL conf.
def createViewSet():
    router = routers.DefaultRouter()
    router.register(r'users', UserViewSet)
    router.register(r'questions', QuestionViewSet)
    router.register(r'choices', ChoiceViewSet)

    return router;
