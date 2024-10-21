import django
from django.http import JsonResponse
from shopping_mall.models import *
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def ShopView(request):
   if request.method == 'GET':
      data = serializers.serialize("json", Shop.objects.all())
      return JsonResponse(json.loads(data[2]), safe=False, status=200)
   elif request.method == 'POST':
      try:
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
         return JsonResponse({"message": "Shop created successfully","data":data[2]}, status=201)
      #   return JsonResponse({"message": "Shop created successfully"}, status=201, data=data, safe=False)
      except django.db.utils.IntegrityError:
         return JsonResponse({"message":"UNIQUE constraint failed"})
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
      return JsonResponse({"message": "Shop updated successfully","data":data[2]}, status=201)
   elif request.method == 'DELETE':
      shop = Shop.objects.get(pk=id)
      has_childeren = Product.objects.filter(shop=shop).exists()
      if has_childeren == False:
         # body = json.loads(request.body.decode("utf-8"))
         Shop.objects.filter(pk=id).delete()
         newrecord = Shop.objects.all()
         data = json.loads(serializers.serialize('json', newrecord))
         return JsonResponse({"message": "Shop deleted successfully","data":data[2]}, status=204)
      else:
         return JsonResponse({"message": "Cannot delete the shop"}, status=403)
   elif request.method == 'GET':
      newrecord = Shop.objects.filter(pk=id)
      data = json.loads(serializers.serialize('json', newrecord))
      return JsonResponse(json.loads(data[2]), safe=False, status=200)
   else:
      return JsonResponse({"message": "Invalid request method"}, status=405)

@csrf_exempt
def CategoryView(request):
   if request.method == 'GET':
      data = serializers.serialize("json", Category.objects.all())
      return JsonResponse(json.loads(data[2]), safe=False, status=200)
   elif request.method == 'POST':
      body = json.loads(request.body.decode("utf-8"))
      newrecord = Category.objects.create(
         name=body['name'],
         description=body['description'],
         image_url=body['image_url'],
      )
      data = json.loads(serializers.serialize('json', [newrecord]))
      return JsonResponse({"message": "Category created successfully","data":data[2]}, status=201)
   else:
      return JsonResponse({"message": "Invalid request method"}, status=405)

@csrf_exempt
def CategoryViewTwo(request, id):
   if request.method == 'PUT':
      body = json.loads(request.body.decode("utf-8"))
      Category.objects.filter(pk=id).update(
         name=body['name'],
         description=body['description'],
         image_url=body['image_url'],
      )
      newrecord = Category.objects.filter(pk=id)
      data = json.loads(serializers.serialize('json', newrecord))
      return JsonResponse({"message": "Category updated successfully","data":data[2]}, status=201)
   elif request.method == 'DELETE':
      # body = json.loads(request.body.decode("utf-8"))
      Category.objects.filter(pk=id).delete()
      newrecord = Category.objects.all()
      data = json.loads(serializers.serialize('json', newrecord))
      return JsonResponse({"message": "Category deleted successfully","data":data[2]}, status=204)
   elif request.method == 'GET':
      newrecord = Category.objects.filter(pk=id)
      data = json.loads(serializers.serialize('json', newrecord))
      return JsonResponse(data[2], safe=False, status=200)
   else:
      return JsonResponse({"message": "Invalid request method"}, status=405)

@csrf_exempt
def ProductView(request):
   if request.method == 'GET':
      data = serializers.serialize("json", Product.objects.all())
      return JsonResponse(json.loads(data[2]), safe=False, status=200)
   elif request.method == 'POST':
      body = json.loads(request.body.decode("utf-8"))
      newrecord = Product.objects.create(
         name=body['name'],
         category=Category.objects.get(pk=body['category']),
         shop=Shop.objects.get(pk=body['shop']),
         brand_name=body['brand_name'],
         price=body['price'],
         discount_price=body['discount_price'],
         image_url=body['image_url'],
         stock_count=body['stock_count'],
         variant=body['variant'],
      )
      data = json.loads(serializers.serialize('json', [newrecord]))
      return JsonResponse({"message": "Product created successfully","data":data[2]}, status=201)
   else:
      return JsonResponse({"message": "Invalid request method"}, status=405)

@csrf_exempt
def ProductViewTwo(request, id):
   if request.method == 'PUT':
      body = json.loads(request.body.decode("utf-8"))
      Product.objects.filter(pk=id).update(
         name=body['name'],
         category=Category.objects.get(pk=body['category']),
         shop=Shop.objects.get(pk=body['shop']),
         brand_name=body['brand_name'],
         price=body['price'],
         discount_price=body['discount_price'],
         image_url=body['image_url'],
         stock_count=body['stock_count'],
         variant=body['variant'],
      )
      newrecord = Product.objects.filter(pk=id)
      data = json.loads(serializers.serialize('json', newrecord))
      return JsonResponse({"message": "Product updated successfully","data":data[2]}, status=201)
   elif request.method == 'DELETE':
      # body = json.loads(request.body.decode("utf-8"))
      Product.objects.filter(pk=id).delete()
      newrecord = Product.objects.all()
      data = json.loads(serializers.serialize('json', newrecord))
      return JsonResponse({"message": "Product deleted successfully","data":data[2]}, status=204)
   elif request.method == 'GET':
      newrecord = Product.objects.filter(pk=id)
      data = json.loads(serializers.serialize('json', newrecord))
      return JsonResponse(data[2], safe=False, status=200)
   else:
      return JsonResponse({"message": "Invalid request method"}, status=405)