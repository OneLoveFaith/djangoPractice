from django.db.models import Count
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import CustomerCl, TagCl, ProductCl, OrderCl
from .forms import OrderForm, ProductForm, TagForm


# TODO add Registration

# class CustomerListView(ListView):
#     model = CustomerCl
#     template_name = 'clothes/customer_list.html'
#     context_object_name = 'customers'


class ProductListView(ListView):
    model = ProductCl
    template_name = 'clothes/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        tag_filter = self.request.GET.get('tag_filter')

        if tag_filter:
            try:
                tag_id = int(tag_filter)
                tag = TagCl.objects.get(id=tag_id)
                return ProductCl.objects.filter(tags=tag)
            except (ValueError, TagCl.DoesNotExist):
                return ProductCl.objects.none()

        return ProductCl.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = TagCl.objects.annotate(num_products=Count('productcl'))
        tag_filter = self.request.GET.get('tag_filter', 0)

        try:
            context['tag_filter'] = int(tag_filter)
        except ValueError:
            context['tag_filter'] = 0

        return context


class ProductCreateView(View):
    template_name = 'clothes/product_create.html'

    def get(self, request):
        form = ProductForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect('product_list')

        return render(request, self.template_name, {'form': form})

class ProductDeleteView(View):
    model = ProductCl

    def post(self, request, *args, **kwargs):
        product_id = kwargs.get('pk')
        product = get_object_or_404(ProductCl, id=product_id)
        product.delete()
        return redirect('product_list')


class AddTagView(View):
    template_name = 'clothes/add_tag.html'

    def get(self, request):
        form = TagForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_create')

        return render(request, self.template_name, {'form': form})


class OrderCreateView(View):
    template_name = 'clothes/order_create.html'

    def get(self, request):
        form = OrderForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect('order_list')

        return render(request, self.template_name, {'form': form})


class OrderListView(ListView):
    model = OrderCl
    template_name = 'clothes/order_list.html'
    context_object_name = 'orders'


class OrderDetailView(DetailView):
    model = OrderCl
    template_name = 'clothes/order_detail.html'
    context_object_name = 'order'


class OrderDeleteView(DeleteView):
    model = OrderCl
    success_url = reverse_lazy('order_list')


class ProductFilterView(ListView):
    model = ProductCl
    context_object_name = 'products'

    def get_queryset(self):
        tag_id = self.kwargs.get('tag_id')
        tag = get_object_or_404(TagCl, id=tag_id)
        return ProductCl.objects.filter(tags=tag)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = get_object_or_404(TagCl, id=self.kwargs.get('tag_id'))
        return context
