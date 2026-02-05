from django.urls import path
from . import views

urlpatterns = [

    # UI
    path('', views.index, name='index'),
    path('dealer/<int:dealer_id>/', views.dealer_page, name='dealer_page'),
    path('add_review/<int:dealer_id>/', views.add_review, name='add_review'),

    # Auth
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    # Q8
    path('fetchReviews/dealer/<int:dealer_id>', views.fetchReviews),

    # Q9
    path('fetchDealers', views.fetchDealers),

    # Q10
    path('fetchDealer/<int:dealer_id>', views.fetchDealer),

    # Q11
    path('fetchDealers/<str:state>', views.fetchDealersState),

    # Q14
    path('get_cars/', views.get_cars),

    # Q15
    path('analyze/<str:text>', views.analyze),
]
