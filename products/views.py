from django.shortcuts import render
from .models import Product
from profiles.models import Profile
from .forms import ProductModelForm
from django.urls import reverse_lazy
from django.views.generic import UpdateView

# Create your views here.

def product_create_list_view(request):
    qs = Product.objects.all()
    profile = Profile.objects.get(user=request.user)

    # # Product form
    # p_form = ProductModelForm()
    # post_add = False

    # # Request author
    # profile = Profile.objects.get(user=request.user)

    # if 'submit_p_form' in request.POST:
    #     p_form = ProductModelForm(request.POST, request.FILES)
    #     if p_form.is_valid():
    #         instance = p_form.save(commit=False)
    #         instance.author = profile
    #         instance.save()
    #         p_form = ProductModelForm()
    #         post_add = True

    context ={
        'qs':qs,
        'profile': profile,
        # 'p_form': p_form,
        # 'post_add': post_add,
    }

    return render(request, 'products/product_list.html', context)

def product_add_list_view(request):
    qs = Product.objects.all()
    profile = Profile.objects.get(user=request.user)

    # Product form
    p_form = ProductModelForm()
    post_add = False

    if 'submit_p_form' in request.POST:
        p_form = ProductModelForm(request.POST, request.FILES)
        if p_form.is_valid():
            instance = p_form.save(commit=False)
            instance.owner = profile
            instance.save()
            p_form = ProductModelForm()
            post_add = True

    context ={
        'qs':qs,
        'profile': profile,
        'p_form': p_form,
        'post_add': post_add,
    }

    return render(request, 'products/add.html', context)

class ProductUpdateView(UpdateView):
    form_class= ProductModelForm
    model = Product
    template_name='products/update.html'
    success_url =  reverse_lazy('products:main-product-view')

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        if not form.instance.owner == profile:
            form.add_error(None, 'You are not the owner of the product')
            return super().form_invalid(form)
        if form.instance.status == "listed":
            form.add_error(None, 'You must cancel the listing of the product first')
            return super().form_invalid(form)
        else:
            return super().form_valid(form) # if valid update the form