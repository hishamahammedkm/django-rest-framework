from django.urls import path
from .views import *
urlpatterns = [
#    path('article/',article_list),
    path('article/',ArticleApiView.as_view()),

    # path('detail/<int:pk>/',article_detail),
    path('detail/<int:id>/',ArticleDetails.as_view()),

]