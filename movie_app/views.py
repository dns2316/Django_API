from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from . import models

# ############################################
# Maybe transfer this part to owned file

# def move_serializer():
#     return serializers.serialize(
#         'json',
#         models.Movie.objects.all(),
#         fields=('name',
#                 'id_imdb',
#                 'created_at',
#                 'updated_at',
#                 'url',
#                 'poster',
#                 'name',
#                 'description',
#                 'year',
#                 ))

# ############################################

# all objects from Movie model
def index(request):
    return serializers.serialize(
        'json',
        models.Movie.objects.all(),
        fields=('name',
                'id_imdb',
                'created_at',
                'updated_at',
                'url',
                'poster',
                'name',
                'description',
                'year',
                ))

# 404 error with custom message
def error(request):
    return HttpResponse(content=f"Staff only!<br>{request.get_full_path()}",
                        status=404)