import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
import requests
from django.views.decorators.csrf import csrf_exempt
from django.utils.html import strip_tags
import json
from django.http import JsonResponse

# Create your views here.

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")
    # limited_items = Product.objects.filter(stock__lt=5).values()

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'npm' : '2406496063',
        'name': request.user.username,
        'class': 'PBP F',
        'product_list' : product_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        # 'limited_items': limited_items
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, description_type="application/xml")

def show_json(request):
    category = request.GET.get('category')
    filter_type = request.GET.get('filter')  # "all" / "my"
    product_list = Product.objects.all()

    if category:
        product_list = product_list.filter(category=category)

    if filter_type == "my" and request.user.is_authenticated:
        product_list = product_list.filter(user=request.user)

    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'product_views': product.product_views,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_featured': product.is_featured,
            'bonus_points': product.bonus_points,
            'stock': product.stock,
            'brand': product.brand,
            'gender': product.gender,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user else None,
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)


def show_xml_by_id(request, product_id):
    try:
        product_list = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_list)
        return HttpResponse(xml_data, description_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    
def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'product_views': product.product_views,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_featured': product.is_featured,
            'bonus_points' : product.bonus_points,
            'stock' : product.stock,
            'brand' : product.brand,
            'gender' : product.gender,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
    
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    if request.method == "POST":

        name = strip_tags(request.POST.get("name"))
        description = strip_tags(request.POST.get("description"))
        category = request.POST.get("category")
        thumbnail = request.POST.get("thumbnail")
        is_featured = request.POST.get("is_featured") == 'on'

        price = int(request.POST.get("price", 0))
        stock = int(request.POST.get("stock", 0))
        bonus_points = int(request.POST.get("bonus_points", 0))
        brand = request.POST.get("brand", "Unknown")
        gender = request.POST.get("gender", "Unisex")

        user = request.user

        new_product = Product(
            name=name,
            description=description,
            category=category,
            thumbnail=thumbnail,
            is_featured=is_featured,
            price=price,
            stock=stock,
            bonus_points=bonus_points,
            brand=brand,
            gender=gender,
            user=user
        )
        new_product.save()

        return JsonResponse({
            "success": True,
            "id": str(new_product.id),
        })
    
    return JsonResponse({"success": False}, status=400)


def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        # Fetch image from external source
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        # Return the image with proper content type
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)
    
@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        name = strip_tags(data.get("name", ""))
        description = strip_tags(data.get("description", ""))
        category = data.get("category", "")
        thumbnail = data.get("thumbnail", "")
        is_featured = data.get("is_featured", False)

        price = data.get("price", 0)
        brand = data.get("brand", "")
        bonus_point = data.get("bonus_point", 0)

        user = request.user

        new_product = Product(
            name=name,
            description=description,
            category=category,
            thumbnail=thumbnail,
            is_featured=is_featured,
            price=price,
            brand=brand,
            bonus_points=bonus_point,
            user=user
        )
        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
