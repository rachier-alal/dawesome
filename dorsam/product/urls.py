from django.urls import include, path

from product import views

urlpatterns = [
    path('latest_products/', views.LatestProductsList.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view())
]
