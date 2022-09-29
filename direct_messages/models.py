from django.db import models
from django.conf import settings
from common.models import CommonModel


class ChattingRoom(CommonModel):

    """ChatiingRoom Model Definition"""

    user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
    )

    def __str__(self):
        return "Chatting Room"


class Message(CommonModel):

    """message Model Definition"""

    text = models.TextField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    room = models.ForeignKey(
        "direct_messages.ChattingRoom",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.user} says: {self.text}"
