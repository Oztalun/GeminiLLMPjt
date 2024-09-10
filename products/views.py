# from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from django.conf import settings
from django.utils import timezone
from . import LLM_Gemini
from .serializers import ProductSerializer


def index(request):
    return render(request, "products/index.html")


def products(request):
    products = Product.objects.all().order_by("-created_at")
    recommend = LLM_Gemini.Get_Answer(ProductSerializer(products, many=True).data)
    print(f"split : {recommend.split()}")
    print(f"map : {list(map(int, recommend.split()))}")
    context = {"products": products, "timediff": timezone.now(), "recommend": list(map(int, recommend.split()))}# 
    return render(request, "products/products.html", context)
# '{{product.title}}'


@require_POST
def like(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=pk)
        if product.like_users.filter(pk=request.user.pk).exists():
            product.like_users.remove(request.user)
        else:
            product.like_users.add(request.user)
    else:
        return redirect("accounts:login")

    return redirect("products:products")


# def new(request):
#     forms = ProductForm()
#     context = {"forms":forms}
#     return render(request, "products/new.html", context)


# def create(request):
#     form = ProductForm(request.POST) # form에 request.POST에 있는 데이터 채워
#     if form.is_valid(): # form 형식에 맞으면
#         product = form.save() # 저장하고 해당 객체 반환
#         return redirect("products:product_detail", product.id)
#     return redirect("products:new")
@login_required
def create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product = form.save()
            return redirect("products:detail", product.id)
    else:
        forms = ProductForm()
    context = {"forms": forms}
    return render(request, "products/new.html", context)


def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    print(product.time_dif())
    # comment_form = CommentForm()
    # comments = product.comments.all()
    # "comment_form":comment_form, "comments":comments
    context = {"product": product, }
    return render(request, "products/detail.html", context)


# def edit(request, pk):
#         context = {"product": Product.objects.get(pk=pk),}
#         return render(request, "product/edit.html", context)


# def update(request, pk):
#     product = Product.objects.get(pk=pk)
#     product.title = request.POST.get("title")
#     product.content = request.POST.get("content")
#     product.save()
#     return redirect("products:product_detail", product.pk)

@login_required
@require_http_methods(["GET", "POST"])
def update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            return redirect("products:detail", product.pk)
    else:
        form = ProductForm(instance=product)
    context = {
        "form": form,
        "product": product,
    }
    return render(request, "products/edit.html", context)


@require_POST
def comment_create(request, pk):
    product = get_object_or_404(Products, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.product = product
        comment.user = request.user
        comment.save()
    return redirect("products:product_detail", product.pk)


@require_POST
def comment_delete(request, pk):  # comment의 pk
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=pk)  # 해당 comment 불러옴
        productid = comment.product
        product = productid.id
        comment.delete()
        return redirect("products:product_detail", product)


@login_required
@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=pk)
        product.delete()
    return redirect("products:products")


# 지우랬는데 안지울거임
def hello(request):
    name = "희경"
    tags = ["python", "django", "html", "css"]
    books = ["해변의 카프카", "코스모스", "백설공주", "어린왕자"]
    context = {
        "name": name,
        "tags": tags,
        "books": books,
    }
    return render(request, "products/hello.html", context)


def data_throw(request):
    return render(request, "products/data_throw.html")


def data_catch(request):
    message = request.GET.get("message")
    context = {"data": message, }
    return render(request, "products/data_catch.html", context)
