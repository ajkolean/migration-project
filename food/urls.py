from django.conf.urls import patterns, include, url
from django.contrib import admin
from migrations import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'food.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^index/', views.index, name='index'),
    url(r'^restaurants/(?P<type_name>\w+)', views.food_type, name='restaurant'),
    )

