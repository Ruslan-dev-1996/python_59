from accounts.views import login_view, logout_view, register_view, user_activate_view
from django.urls import path
urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('activate/<token>/', user_activate_view, name='user_activate')
]

app_name = 'accounts'