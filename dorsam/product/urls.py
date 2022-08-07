from django.urls import include, path

from product import views

urlpatterns = [
    path('latest_products/', views.LatestProductsList.as_view()),
]
