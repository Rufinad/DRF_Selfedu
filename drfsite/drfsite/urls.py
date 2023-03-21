from django.contrib import admin
from django.urls import path, include

from women.views import *
from rest_framework import routers


# class MyCustomRouter(routers.SimpleRouter):
#     routes = [
#         routers.Route(url=r'^{prefix}{trailing_slash}$',
#                       mapping={'get': 'list'},
#                       name='{basename}-list',
#                       detail=False,
#                       initkwargs={'suffix': 'List'}),
#         routers.Route(url=r'^{prefix}/{lookup}$',
#                       mapping={'get': 'retrieve'},
#                       name='{basename}-detail',
#                       detail=True,
#                       initkwargs={'suffix': 'Detail'})
#     ]


# router = MyCustomRouter()  # http://127.0.0.1:8000/api/v1/ в Simplerouter такого нет
# router.register(r'women', WomenViewSet, basename='women')
# print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/women/', WomenAPIList.as_view()),
    path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>/', WomenAPIDestroy.as_view()),
]