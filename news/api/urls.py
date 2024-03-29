from django.urls import path
# from news.api.views import article_list_create_api_view, article_detail_api_view
from news.api.views import Article_List_Create_API_View, Article_Detail_API_View, Journalist_List_Create_API_View

urlpatterns =[
    path("articles/", Article_List_Create_API_View.as_view(), name="article-list"),
    path("articles/<int:pk>/", Article_Detail_API_View.as_view(), name="article-detail"),
    path("journalists/", Journalist_List_Create_API_View.as_view(), name="journalist-list"),
    # path("articles/", article_list_create_api_view, name="article-list"),
    # path("articles/<int:pk>/", article_detail_api_view, name="article-detail"),
  
]