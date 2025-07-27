from django.urls import path
from .views import SubmitRatingView, UserRatingHistoryView

urlpatterns = [
    path('submit/', SubmitRatingView.as_view(), name='submit_rating'),
    path('history/<str:user_id>/', UserRatingHistoryView.as_view(), name='rating_history'),
]
