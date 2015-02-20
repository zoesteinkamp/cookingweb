from django.conf.urls import patterns, include, url
from django.contrib import admin
from Recipes import views
from Recipes.views import MainPhotoList, MainPhotoDetail

urlpatterns = [
    url(r'^mainphoto/$', views.MainPhotoList.as_view() ),
    url(r'^mainphoto/(?P<pk>[0-9]+)/$', views.MainPhotoDetail.as_view()),
    url(r'^recipe/$', views.RecipeList.as_view() ),
    url(r'^recipe/(?P<pk>[0-9]+)/$', views.RecipeDetail.as_view()),
    url(r'^ingredient/$', views.IngredientList.as_view() ),
    url(r'^ingredient/(?P<pk>[0-9]+)/$', views.IngredientDetail.as_view()),
    url(r'^tag/$', views.TagList.as_view() ),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagDetail.as_view()),
    url(r'^comment/$', views.CommentList.as_view() ),
    url(r'^comment/(?P<pk>[0-9]+)/$', views.CommentDetail.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', views.home)

]