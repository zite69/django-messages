from django.views.generic import RedirectView
from django.urls import include, re_path
from django_messages.views import *

urlpatterns = [
    re_path('', RedirectView.as_view(permanent=True, url='inbox/'), name='messages_redirect'),
    re_path('inbox/', inbox, name='messages_inbox'),
    re_path('outbox/', outbox, name='messages_outbox'),
    re_path('compose/', compose, name='messages_compose'),
    re_path('compose/(?P<recipient>[\w.@+-]+)/', compose, name='messages_compose_to'),
    re_path('reply/(?P<message_id>[\d]+)/', reply, name='messages_reply'),
    re_path('view/(?P<message_id>[\d]+)/', view, name='messages_detail'),
    re_path('delete/(?P<message_id>[\d]+)/', delete, name='messages_delete'),
    re_path('undelete/(?P<message_id>[\d]+)/', undelete, name='messages_undelete'),
    re_path('trash/$', trash, name='messages_trash'),
]
