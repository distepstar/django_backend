from django.http import Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm


# Create your views here.

# Example
def product_delete_view(request, my_id, *args, **kwargs):
    obj = get_object_or_404(Product, id=my_id)
    # POST REQUEST
    if request.method == 'POST':
        # confiming delete
        obj.delete()
        return redirect('../')

    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)



def dynamic_lookup_view(request, my_id, *args, **kwargs):
    obj = Product.objects.get(id=my_id)
    context = {
        "object": obj
    }

    return render(request, "products/product_detail.html", context)

def render_initial_data(request, *args, **kwargs):
    init_data = {
        'title': "My awesome title"
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, initial=init_data, instance=obj)
    context = {
        'form': form
    }

    return render(request, "products/product_create.html", context)
# def product_create_view(request, *args, **kwargs):
#     # django validation
#     my_form = RawProductForm()
#     if request.method == 'POST':
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             # creating new object to database
#             # ** -> turn into argument
#             Product.objects.create(**my_form.cleaned_data)
#             my_form = RawProductForm()
#         else:
#             print(my_form.errors)

#     context = {
#         "form": my_form
#     }


#     return render(request, 'products/product_create.html', context)
# def product_create_view(request, *args, **kwargs):

#     if request.method == 'POST':
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
#         # Product.objects.create(title=my_new_title)
#     context = {}
#     return render(request, 'products/product_create.html', context)

def product_create_view(request, *args, **kwargs):
    # success and render a form or render a empty form
    init_data = {
        'title': "My awesome title"
    }

    obj = Product.objects.get(id=1)

    form = ProductForm(request.POST or None, initial=init_data, instance=obj)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form,
    }
    return render(request, 'products/product_create.html', context)


# my_id = default None
def product_detail_view(request, my_id=None, *args, **kwargs):
    obj = Product.objects.all()
    if my_id != None:
            # List object
            # obj = get_list_or_404(Product.objects.filter(id=my_id))
        try:
            # Queryset object
            obj = Product.objects.filter(id=my_id)
            # raising the exception for catching
            if bool(obj) == False:
                raise Product.DoesNotExist
        except Product.DoesNotExist:
            raise Http404
        
    context = {
        'object': obj,
    }
    return render(request, 'products/product_detail.html', context)