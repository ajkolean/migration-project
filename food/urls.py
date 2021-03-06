from django.conf.urls import patterns, include, url
from django.contrib import admin
from migrations import views
from migrations.views import HomeView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'food.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^foods', views.list_foods.as_view()),
    url(r'^restaurants/(?P<type_name>\w+)', views.list_restaurants.as_view(), name='restaurants'),
    url(r'$', HomeView.as_view()),
    #url(r'^restaurants/\w+/(?P<name>\w+)', views.restaurant_detail.as_view(), name='restaurant')
    )
