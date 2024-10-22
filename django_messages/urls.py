from django.views.generic import RedirectView
from django.urls import re_path, path
from django_messages.views import *

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='messages_inbox'), name='messages_redirect'),
    path('inbox/', inbox, name='messages_inbox'),
    path('outbox/', outbox, name='messages_outbox'),
    path('compose/', compose, name='messages_compose'),
    re_path(r'compose/(?P<recipient>[\w.@+-]+)/', compose, name='messages_compose_to'),
    re_path(r'reply/(?P<message_id>[\d]+)/', reply, name='messages_reply'),
    re_path(r'view/(?P<message_id>[\d]+)/', view, name='messages_detail'),
    re_path(r'delete/(?P<message_id>[\d]+)/', delete, name='messages_delete'),
    re_path(r'undelete/(?P<message_id>[\d]+)/', undelete, name='messages_undelete'),
    path('trash/', trash, name='messages_trash'),
]
