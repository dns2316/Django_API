from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, JsonResponse, Http404
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from . import models

# all objects from Movie model
@require_http_methods(["GET"])
def index(request):
    return HttpResponse(serializers.serialize(
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
                )), content_type='application/json')


# get movie by id
@require_http_methods(["GET"])
def movie(request, movie_id):
    try:
        movie_data = models.Movie.objects.filter(pk=movie_id)

        if not movie_data:
            raise Http404("Movie does not exist")
        else:
            return HttpResponse(serializers.serialize(
                'json',
                movie_data,
                fields=('name',
                        'id_imdb',
                        'created_at',
                        'updated_at',
                        'url',
                        'poster',
                        'name',
                        'description',
                        'year'
                        )), content_type='application/json')

    except ObjectDoesNotExist:
        raise Http404("Movie does not exist")


# 404 error with custom message
def error(request):
    return HttpResponse(content=f"Staff only!<br>{request.get_full_path()}",
                        status=404)