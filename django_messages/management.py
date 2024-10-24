from django.db.models import signals
from django.conf import settings

if "pinax.notifications" in settings.INSTALLED_APPS and getattr(settings, 'DJANGO_MESSAGES_NOTIFY', True):
    from pinax.notifications import models as notification

    def create_notice_types(app, created_models, verbosity, **kwargs):
        notification.create_notice_type("messages_received", "Message Received", "you have received a message", default=2)
        notification.create_notice_type("messages_sent", "Message Sent", "you have sent a message", default=1)
        notification.create_notice_type("messages_replied", "Message Replied", "you have replied to a message", default=1)
        notification.create_notice_type("messages_reply_received", "Reply Received", "you have received a reply to a message", default=2)
        notification.create_notice_type("messages_deleted", "Message Deleted", "you have deleted a message", default=1)
        notification.create_notice_type("messages_recovered", "Message Recovered", "you have undeleted a message", default=1)

    signals.post_syncdb.connect(create_notice_types, sender=notification)
else:
    print("Skipping creation of NoticeTypes as notification app not found")
