from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('parent-register/', views.parent_register, name='parent_register'),
    path('logout/', views.logout_view, name='logout'),
    path('notifications/', views.notification_list, name='notification'),
    path('competition/', views.competition_list, name='competition'),
    path('membership/', views.player_list, name='membership'),
    path('join/', views.join_player, name='join_player'),
    path('add-notification/', views.add_notification, name='add_notification'),
    path('add-competition/', views.add_competition, name='add_competition'),
    # path('update-notification/<int:notification_id>/', views.update_notification, name='update_notification'),
    # path('delete-notification/<int:notification_id>/', delete_notification, name='delete_notification'),





    




]

