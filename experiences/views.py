from django.db import transaction
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound, ParseError
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from .models import Perk, Experience
from . import serializers
from categories.models import Category


class Perks(APIView):
    def get(self, request):
        all_perks = Perk.objects.all()
        serializer = serializers.PerkSerializer(
            all_perks,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.PerkSerializer(data=request.data)
        if serializer.is_valid():
            perk = serializer.save()
            return Response(serializers.PerkSerializer(perk).data)
        else:
            return Response(serializer.errors)


class PerkDetail(APIView):
    def get_object(self, pk):
        try:
            return Perk.objects.get(pk=pk)
        except Perk.DoesNotExist:
            return NotFound

    def get(self, request, pk):
        perk = self.get_object(pk)
        serializer = serializers.PerkSerializer(perk)
        return Response(serializer.data)

    def put(self, request, pk):
        perk = self.get_object(pk)
        serializer = serializers.PerkSerializer(
            perk,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_perk = serializer.save()
            return Response(
                serializers.PerkSerializer(updated_perk).data,
            )
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        perk = self.get_object(pk)
        perk.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class Experiences(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_experiences = Experience.objects.all()
        serializer = serializers.ExperienceListSerializer(
            all_experiences,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.ExperienceDetailSerializer(data=request.data)
        if serializer.is_valid():
            experience = serializer.save()
            serializer = serializers.ExperienceDetailSerializer(experience)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    # def post(self, request):
    #     serializer = serializers.ExperienceDetailSerializer(
    #         data=request.data,
    #     )
    #     if serializer.is_valid():
    #         category_pk = request.data.get("category")
    #         if not category_pk:
    #             raise ParseError("Category is required.")
    #         try:
    #             category = Category.objects.get(pk=category_pk)
    #             if category.kind == Category.CategoryKindChoices.ROOMS:
    #                 raise ParseError("The Category Kind Shold be 'Experience'")
    #         except Category.DoesNotExist:
    #             raise ParseError("Category not found")
    #         try:
    #             with transaction.atomic():
    #                 experience = serializer.save(
    #                     owner=request.user,
    #                     category=category,
    #                 )
    #                 perks = request.data.get("perks")
    #                 print(dict(perks))
    #                 for perk_pk in perks:
    #                     perk = Perk.objects.get(pk=perk_pk)
    #                     print(perk_pk)
    #                     experience.perks.add(perk)
    #                 serializer = serializers.ExperienceDetailSerializer(experience)
    #                 return Response(serializer.data)
    #         except Exception:
    #             raise ParseError("Perk not found")
    #     else:
    #         return Response(serializer.errors)


class ExperienceDetail(APIView):
    pass


class ExperiencePerk(APIView):
    pass


class ExperienceBookings(APIView):
    pass


class ExperienceBookingDetail(APIView):
    pass
