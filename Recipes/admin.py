from django.contrib import admin
from Recipes.models import Recipe, Ingredients, MainPhoto, Tag, Comment


@admin.register(Recipe)
class Recipe(admin.ModelAdmin):
    list_filter=('title','author','short_des','long_des','servings','prep_time','cook_time','slug','vegan','vegeterian','glutten_free','dairy_free','date','photo')
    filter_horizontal = ('ingredients','tags',)

@admin.register(Ingredients)
class Ingredients(admin.ModelAdmin):
    list_filter=('name','amount','type')

@admin.register(MainPhoto)
class MainPhoto(admin.ModelAdmin):
    list_filter= ('name','image_main',)

@admin.register(Tag)
class Tag(admin.ModelAdmin):
    list_filter = ('tag',)

@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_filter = ('recipe', 'name','body','rating','created')