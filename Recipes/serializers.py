from rest_framework import serializers
from Recipes.models import MainPhoto, Recipe, Ingredients, Tag, Comment


class MainPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPhoto
        fields = ('image_main','name')

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ('name','amount','type')

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True , read_only=True)
    photo = MainPhotoSerializer()
    class Meta:
        model = Recipe
        fields = ('title','author','short_des','long_des','slug','date','servings','prep_time','cook_time','vegan','ingredients','vegeterian','glutten_free','dairy_free','photo','tags')
        read_only_fields = ('id', 'date')



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('name','body','rating','created','recipe')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields =('tag',)

