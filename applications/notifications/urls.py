from django.conf.urls import url
from applications.notifications import views
from django.views.decorators.csrf import csrf_protect


urlpatterns = [

    # Show notification page
    url(r'^notifications/$', views.notifications_page, name='notifications'),
    # Mark as read when clicked on notification and redirect
    url(r'^notification/(?P<notification_id>[^/]+)/redirect/$',
        views.notification_redirect, name='notification_redirect'),
    # Mark notification as read
    url(r'^ajax/notifications/read/(?P<notification_id>[^/]+)$',
        views.notifications_read, name='notifications_read'),
    url(r'^ajax/notifications/read/$',
        views.notifications_read, name='notifications_read'),
    # Get number of notifications in each group
    url(r'^ajax/notifications/group-count/$', views.notification_count_per_group,
        name='notification_count_per_group'),
    # Show notifications
    url(r'^ajax/notifications/$', views.notifications_ajax_api,
        name='notifications_ajax_api'),
]
