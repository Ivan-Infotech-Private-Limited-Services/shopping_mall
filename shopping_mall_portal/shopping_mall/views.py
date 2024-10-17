from django.http import JsonResponse
from shopping_mall.models import *
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def ShopView(request):
   if request.method == 'GET':
      data = serializers.serialize("json", Shop.objects.all())
      return JsonResponse(json.loads(data), safe=False)
   elif request.method == 'POST':
      body = json.loads(request.body.decode("utf-8"))
      newrecord = Shop.objects.create(
         name=body['name'],
         description=body['description'],
         owner_name = body['owner_name'],
         shop_no = body['shop_no'],
         address = body['address'],
         phone1 = body['phone1'],
         phone2 = body['phone2'],
         image_url=body['image_url'],
         )
      data = json.loads(serializers.serialize('json', [newrecord]))
      return JsonResponse({"message": "Shop created successfully","data":data})
    #   return JsonResponse({"message": "Shop created successfully"}, status=201, data=data, safe=False)
   else:
      return JsonResponse({"message": "Invalid request method"}, status=405)

@csrf_exempt
def ShopViewTwo(request, id):
   if request.method == 'PUT':
      body = json.loads(request.body.decode("utf-8"))
      Shop.objects.filter(pk=id).update(
         name=body['name'],
         description=body['description'],
         owner_name = body['owner_name'],
         shop_no = body['shop_no'],
         address = body['address'],
         phone1 = body['phone1'],
         phone2 = body['phone2'],
         image_url=body['image_url'],
      )
      newrecord = Shop.objects.filter(pk=id)
      data = json.loads(serializers.serialize('json', newrecord))
      return JsonResponse({"message": "Shop updated successfully","data":data})
   elif request.method == 'DELETE':
      # body = json.loads(request.body.decode("utf-8"))
      Shop.objects.filter(pk=id).delete()
      newrecord = Shop.objects.all()
      data = json.loads(serializers.serialize('json', newrecord))
      return JsonResponse({"message": "Shop deleted successfully","data":data})
   elif request.method == 'GET':
      newrecord = Shop.objects.filter(pk=id)
      data = json.loads(serializers.serialize('json', newrecord))
      return JsonResponse(data, safe=False)
   else:
      return JsonResponse({"message": "Invalid request method"}, status=405)