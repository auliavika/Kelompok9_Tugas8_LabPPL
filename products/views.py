from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .form import ProductForm
from django.contrib import messages

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/list.html', {'products': products})

def product_create(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Produk berhasil ditambahkan!')
        return redirect('product_list')
    return render(request, 'products/form.html', {'form': form})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        messages.success(request, 'Produk berhasil diperbarui!')
        return redirect('product_list')
    return render(request, 'products/form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    messages.success(request, 'Produk berhasil dihapus!')
    return redirect('product_list')
