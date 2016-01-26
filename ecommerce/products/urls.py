from django.conf.urls import url
from .views import (
    ProductListView,
    ProductDetailView,
    )
    #VariationListView,
    #CategoryListView,
    #CategoryDetailView,
    #)

urlpatterns = [
    url(r'^$', ProductListView, name='list'),
    url(r'^(?P<pk>\d+)/$', ProductDetailView),
    #url(r'^(?P<id>\d+)/$', VariationListView, name='detail'),
    #url(r'^(?P<id>\d+)/edit/$', blog_update, name='update'),
    #url(r'^(?P<id>\d+)/delete/$', blog_delete),
]


# pahlay yeh do views chala lain phir baki chala lain ge