from rest_framework.serializers import ModelSerializer
from .models import Perk, Experience
from users.serializers import TinyUserSerializer


class PerkSerializer(ModelSerializer):
    class Meta:
        model = Perk
        fields = "__all__"


class ExperienceListSerializer(ModelSerializer):
    host = TinyUserSerializer(
        read_only=True,
    )
    perks = PerkSerializer(
        read_only=True,
        many=True,
    )

    class Meta:
        model = Experience
        fields = (
            "country",
            "city",
            "name",
            "host",
            "address",
            "start",
            "end",
            "perks",
            "description",
            "category",
        )


class ExperienceDetailSerializer(ModelSerializer):
    perks = PerkSerializer(
        read_only=True,
        many=True,
    )

    class Meta:
        model = Experience
        fields = "__all__"
