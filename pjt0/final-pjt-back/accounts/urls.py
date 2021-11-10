from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path
from .views import UserCDView, UserView, UserId


urlpatterns = [
    path('api-token-auth/', obtain_jwt_token),
    path('user/', UserCDView.as_view()),
    path('<int:user_id>/detail/', UserView.as_view()),
    path('id/<username>/', UserId.as_view()),
]
