from django.urls import path
from .views import pictureLike, pictureDislike, getAllLikes, getAll

urlpatterns = [
    path('like/<int:pic_id>/', pictureLike),
    path('dislike/<int:pic_id>/', pictureDislike),
    path('get_all_likes/', getAllLikes),
    path('get_all/', getAll)
]
