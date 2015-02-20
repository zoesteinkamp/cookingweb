from django.template import RequestContext
from rest_framework import permissions
from rest_framework import generics
from Recipes.forms import CommentForm
from Recipes.models import MainPhoto, Recipe, Ingredients, Tag, Comment
from Recipes.serializers import MainPhotoSerializer, RecipeSerializer, IngredientSerializer, TagSerializer, \
    CommentSerializer
from django.shortcuts import render, redirect, render_to_response, get_object_or_404


def home(request):
    return render(request, 'help.html')


class MainPhotoList(generics.ListCreateAPIView):    # This will list all the menu items, its using generics to create a new list
    queryset = MainPhoto.objects.all()              # It grabs all the data
    serializer_class = MainPhotoSerializer          # Then grabs the serializer class, basically organizing the data to display
    permission_classes = [
         permissions.AllowAny
    ]

class MainPhotoDetail(generics.RetrieveUpdateDestroyAPIView): # So now using generics we can retireve the data and either update
    queryset = MainPhoto.objects.all()                        # or we can destroy it
    serializer_class = MainPhotoSerializer
    permission_classes = [
         permissions.AllowAny
    ]

class RecipeList(generics.ListCreateAPIView):    # This will list all the menu items, its using generics to create a new list
    queryset = Recipe.objects.all()              # It grabs all the data
    serializer_class = RecipeSerializer          # Then grabs the serializer class, basically organizing the data to display
    permission_classes = [
         permissions.AllowAny
    ]

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView): # So now using generics we can retireve the data and either update
    queryset = Recipe.objects.all()                        # or we can destroy it
    serializer_class = RecipeSerializer
    permission_classes = [
         permissions.AllowAny
    ]

class IngredientList(generics.ListCreateAPIView):    # This will list all the menu items, its using generics to create a new list
    queryset = Ingredients.objects.all()              # It grabs all the data
    serializer_class = IngredientSerializer          # Then grabs the serializer class, basically organizing the data to display
    permission_classes = [
         permissions.AllowAny
    ]

class IngredientDetail(generics.RetrieveUpdateDestroyAPIView): # So now using generics we can retireve the data and either update
    queryset = Ingredients.objects.all()                        # or we can destroy it
    serializer_class = IngredientSerializer
    permission_classes = [
         permissions.AllowAny
    ]

class TagList(generics.ListCreateAPIView):    # This will list all the menu items, its using generics to create a new list
    queryset = Tag.objects.all()              # It grabs all the data
    serializer_class = TagSerializer          # Then grabs the serializer class, basically organizing the data to display
    permission_classes = [
         permissions.AllowAny
    ]

class TagDetail(generics.RetrieveUpdateDestroyAPIView): # So now using generics we can retireve the data and either update
    queryset = Tag.objects.all()                        # or we can destroy it
    serializer_class = TagSerializer
    permission_classes = [
         permissions.AllowAny
    ]
class CommentList(generics.ListCreateAPIView):    # This will list all the menu items, its using generics to create a new list
    queryset = Comment.objects.all()              # It grabs all the data
    serializer_class = CommentSerializer          # Then grabs the serializer class, basically organizing the data to display
    permission_classes = [
         permissions.AllowAny
    ]

class CommentDetail(generics.RetrieveUpdateDestroyAPIView): # So now using generics we can retireve the data and either update
    queryset = Comment.objects.all()                        # or we can destroy it
    serializer_class = CommentSerializer
    permission_classes = [
         permissions.AllowAny
    ]