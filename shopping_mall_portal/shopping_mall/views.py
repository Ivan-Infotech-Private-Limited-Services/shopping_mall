from django.http import JsonResponse
from shopping_mall.models import *
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def ShopView(request):
   if request.method == 'GET':
      data = serializers.serialize("json", Shop.objects.all())
      return JsonResponse(json.loads(data['fields']), safe=False)
   elif request.method == 'POST':
      body = json.loads(request.body.decode("utf-8"))
      unique_value = request.POST.get('shop_no')
      unique_value2 = request.POST.get('phone1')
      unique_value3 = request.POST.get('phone2')
      if Shop.objects.filter(shop_no=unique_value).exists() or Shop.objects.filter(phone1=unique_value2).exists() or Shop.objects.filter(phone2=unique_value3).exists():
         return JsonResponse({"message": "Shop number, phone1 or phone2 already exists"}, status=409)
      else:
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
         return JsonResponse({"message": "Shop created successfully","data":data['fields']})
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
      return JsonResponse({"message": "Shop updated successfully","data":data['fields']})
   elif request.method == 'DELETE':
      shop = Shop.objects.get(pk=id)
      has_childeren = Product.objects.filter(parent=shop).exists()
      if has_childeren == False:
         # body = json.loads(request.body.decode("utf-8"))
         Shop.objects.filter(pk=id).delete()
         newrecord = Shop.objects.all()
         data = json.loads(serializers.serialize('json', newrecord))
         return JsonResponse({"message": "Shop deleted successfully","data":data['fields']})
      else:
         return JsonResponse({"message": "Cannot delete the shop"}, status=404)
   elif request.method == 'GET':
      newrecord = Shop.objects.filter(pk=id)
      data = json.loads(serializers.serialize('json', newrecord))
      return JsonResponse(data['fields'], safe=False)
   else:
      return JsonResponse({"message": "Invalid request method"}, status=405)

@csrf_exempt
def CategoryView(request):
   if request.method == 'GET':
      data = serializers.serialize("json", Category.objects.all())
      return JsonResponse(json.loads(data), safe=False)
   elif request.method == 'POST':
      body = json.loads(request.body.decode("utf-8"))
      newrecord = Category.objects.create(
         name=body['name'],
         description=body['description'],
         image_url=body['image_url'],
      )
      data = json.loads(serializers.serialize('json', [newrecord]))
      return JsonResponse({"message": "Category created successfully","data":data['fields']})
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
      return JsonResponse({"message": "Category updated successfully","data":data})
   elif request.method == 'DELETE':
      # body = json.loads(request.body.decode("utf-8"))
      Category.objects.filter(pk=id).delete()
      newrecord = Category.objects.all()
      data = json.loads(serializers.serialize('json', newrecord))
      return JsonResponse({"message": "Category deleted successfully","data":data['fields']})
   elif request.method == 'GET':
      newrecord = Category.objects.filter(pk=id)
      data = json.loads(serializers.serialize('json', newrecord))
      return JsonResponse(data, safe=False)
   else:
      return JsonResponse({"message": "Invalid request method"}, status=405)

@csrf_exempt
def ProductView(request):
   if request.method == 'GET':
      data = serializers.serialize("json", Product.objects.all())
      return JsonResponse(json.loads(data['fields']), safe=False)
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
      return JsonResponse({"message": "Product created successfully","data":data['fields']})
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
      return JsonResponse({"message": "Product updated successfully","data":data['fields']})
   elif request.method == 'DELETE':
      # body = json.loads(request.body.decode("utf-8"))
      Product.objects.filter(pk=id).delete()
      newrecord = Product.objects.all()
      data = json.loads(serializers.serialize('json', newrecord))
      return JsonResponse({"message": "Product deleted successfully","data":data['fields']})
   elif request.method == 'GET':
      newrecord = Product.objects.filter(pk=id)
      data = json.loads(serializers.serialize('json', newrecord))
      return JsonResponse(data['fields'], safe=False)
   else:
      return JsonResponse({"message": "Invalid request method"}, status=405)