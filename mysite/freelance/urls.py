from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('skill/', SkillListAPIView.as_view(), name='skill_list'),

    path('user/', UserProfileListAPIView.as_view(), name='user_list'),
    path('user_my/', UserProfileListOwnAPIView.as_view(), name='own_user_list'),
    path('user_my/<int:pk>/', UserProfileEditAPIView.as_view(), name='user_edit'),

    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),

    path('project/', ProjectListAPIView.as_view(), name='project_list'),
    path('project/<int:pk>/', ProjectDetailAPIView.as_view(), name='project_detail'),
    path('project/create/', ProjectAPIView.as_view(), name='project_create'),

    path('project_my/', ProjectListAPIView.as_view(), name='project_create'),
    path('project_my/<int:pk>/', ProjectDetailOwnAPIView.as_view(), name='project_create'),

    path('offer/', OfferListAPIView.as_view(), name='offer_list'),
    path('offer/create/', OfferAPIView.as_view(), name='offer_create'),
    path('offer/<int:pk>/', OfferEditAPIView.as_view(), name='offer_edit'),

    path('reviews/create/', ReviewAPIView.as_view(), name='reviews_create'),
]
