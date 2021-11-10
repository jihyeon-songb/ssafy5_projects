from django.urls import path
from .views import CollectionView, CollectionListView, MovieListView, CollecionAllView, SearchMovie

urlpatterns = [
    path('collection/<int:collection_id>/', CollectionView.as_view()),
    path('collection_list/<int:user_id>/', CollectionListView.as_view()),
    path('collections_all/', CollecionAllView.as_view()),
    path('search/', SearchMovie.as_view()),
    path('movie/', MovieListView.as_view()),
]
