from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('get_dealers/', views.get_dealers, name='get_dealers'),
    path('get_dealers/<str:state>/', views.get_dealers_by_state, name='get_dealers_by_state'),
    path('get_dealer/<int:dealer_id>/', views.get_dealer_details, name='get_dealer_details'),

    # 🔴 THIS IS THE IMPORTANT ONE
    path('add_review/<int:dealer_id>/', views.add_review, name='add_review'),
]
