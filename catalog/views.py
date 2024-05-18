from django.shortcuts import render

from catalog.models import Product, Category


def products_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, "products_temp.html", context)

# # def contacts(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         phone = request.POST.get("phone")
#         message = request.POST.get("message")
#         print(f"name: {name}\nphone: {phone}\nmessage: {message}")
#     return render(request, "contact.html")
