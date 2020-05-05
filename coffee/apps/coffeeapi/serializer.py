from rest_framework import serializers
from .models import(
    BeanInfo, CoffeeInfo
)
class BeanInfoSerializer(serializers.ModelSerializer): #passing serializers from another app to this one

    owner = serializers.ReadOnlyField(source='owner.username') #owner is the instance coming from the model

    class Meta:
        model = BeanInfo #telling which model we want
        fields = ('id','name','description', 'owner','category','ingredients','directions', 'created_at', 'updated_at', 'is_public')
        #wanting to pass a foreign key so we want to mention owner outside of the foreign key before Meta

class CoffeeInfoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # owner is the instance coming from the model
    # we defined owner in the model as a foreign key, the foreign key brings the data
    beans = BeanInfoSerializer(many=True, read_only=True, required=False) # many recipes is a possibility, therefore true
    class Meta:
        model = CoffeeInfo
        fields = ('id','name','owner', 'description','recipies', 'created_at', 'updated_at')