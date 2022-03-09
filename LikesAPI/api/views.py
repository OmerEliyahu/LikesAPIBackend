import requests
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from .models import Picture
from django.db.models import Q
import csv


@api_view(['POST'])
def pictureLike(request, pic_id):
    try:
        pic_id = int(pic_id)
    except ValueError:
        return HttpResponse(status=400)
    pic = None
    try:
        pic = Picture.objects.get(id=pic_id)
        pic.likes += 1
        pic.save()
    except ObjectDoesNotExist:
        return HttpResponse(status=400)
    finally:
        return HttpResponse(pic.likes, status=200)


@api_view(['POST'])
def pictureDislike(request, pic_id):
    try:
        pic_id = int(pic_id)
    except ValueError:
        return HttpResponse(status=400)
    pic = None
    try:
        pic = Picture.objects.get(id=pic_id)
    except ObjectDoesNotExist:
        return HttpResponse(status=400)
    finally:
        pic.dislikes += 1
        pic.save()
        return HttpResponse(pic.dislikes, status=200)


@api_view(['GET'])
def getAll(request):
    pics = list(Picture.objects.all().values())
    if len(pics) == 0:
        pics_to_create = []
        r = requests.get('https://picsum.photos/v2/list?page=1&limit=100')
        for pic in r.json():
            pics_to_create.append(Picture(id=pic['id'], url=pic['download_url']))
        Picture.objects.bulk_create(pics_to_create)
    return JsonResponse(list(Picture.objects.all().values()), safe=False)


@api_view(['GET'])
def getAllLikes(request):
    all_likes = list(Picture.objects.filter(~Q(likes=0) | ~Q(dislikes=0)).all().values())
    keys = all_likes[0].keys()
    with open('likes.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(all_likes)

    with open('likes.csv') as myfile:
        response = HttpResponse(myfile, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=likes.csv.csv'
        return response


