from django.shortcuts import render
from .models import Product
from profiles.models import Profile
from .forms import ProductModelForm, ProductUpdateForm, ProductSellForm, ProductBuyForm
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView
from django.db.models import Q

# Create your views here.


def product_create_list_view(request):
    qs = Product.objects.all()
    query=''
    if 'q' in request.GET:
        query = request.GET.get('q')
        queryset = (Q(tags__icontains=query))
        qs = Product.objects.filter(queryset).distinct()
    
    profile = Profile.objects.get(user=request.user)

    context = {
        'qs': qs,
        'profile': profile,
        'query': query,
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

    context = {
        'qs': qs,
        'profile': profile,
        'p_form': p_form,
        'post_add': post_add,
    }

    return render(request, 'products/add.html', context)


class ProductUpdateView(UpdateView):
    form_class = ProductUpdateForm
    model = Product
    template_name = 'products/update.html'
    success_url = reverse_lazy('products:main-product-view')

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        if not form.instance.owner == profile:
            form.add_error(None, 'You are not the owner of the product')
            return super().form_invalid(form)
        if form.instance.status == "listed":
            form.add_error(
                None, 'You must cancel the listing of the product first')
            return super().form_invalid(form)
        else:
            return super().form_valid(form)  # if valid update the form


class ProductSellView(UpdateView):
    form_class = ProductSellForm
    model = Product
    template_name = 'products/sell.html'
    success_url = reverse_lazy('products:main-product-view')

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        print(form.instance.status)
        if not form.instance.owner == profile:
            form.add_error(None, 'You are not the owner of the product')
            return super().form_invalid(form)
        else:
            form.instance.status = "listed"
            return super().form_valid(form)  # if valid update the form


class ProductCancelView(UpdateView):
    form_class = ProductBuyForm
    model = Product
    template_name = 'products/cancel.html'
    success_url = reverse_lazy('products:main-product-view')

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        if not form.instance.owner == profile:
            form.add_error(None, 'You are not the owner of the product')
            return super().form_invalid(form)
        else:
            form.instance.status = "owned"
            return super().form_valid(form)  # if valid update the form


class ProductBuyView(UpdateView):
    form_class = ProductBuyForm
    model = Product
    template_name = 'products/buy.html'
    success_url = reverse_lazy('products:product-buy-success')

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        if form.instance.owner == profile:
            form.add_error(None, 'You are the owner of the product')
            return super().form_invalid(form)
        if form.instance.price > profile.credit:
            form.add_error(None, 'You don\'t have enough money')
            return super().form_invalid(form)
        else:
            print(form.instance.owner.credit)
            form.instance.owner.credit = form.instance.owner.credit + form.instance.price
            form.instance.owner.save()
            form.instance.owner = profile
            form.instance.status = "owned"
            profile.credit = profile.credit - form.instance.price
            profile.save()
            return super().form_valid(form)  # if valid update the form


def product_post_buy(request):
    qs = Product.objects.all()
    profile = Profile.objects.get(user=request.user)

    context = {
        'qs': qs,
        'profile': profile,
    }

    return render(request, 'products/buy_success.html', context)

