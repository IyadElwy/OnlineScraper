from django.urls import path
from . import views

urlpatterns = [
    path('', views.WebsiteProductListView.as_view(), name='home'),
    path('addwebsite/', views.AddWebsiteView.as_view(), name='create_website'),
    path('addproduct/', views.ProductCreateView.as_view(), name='create_product'),
    path('settings/<int:pk>/', views.SettingsDetailView.as_view(), name='settings'),
    path('settings/<int:pk>/edit/', views.SettingsUpdateView.as_view(), name='settings_update'),
    path('websites/<int:pk>/', views.WebsiteDetailView.as_view(), name='website'),
    path('websites/<int:pk>/delete/', views.DeleteWebsiteView.as_view(), name='website_delete'),
    path('products/<int:pk>/', views.ProductUpdateView.as_view(), name='product'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),

]
