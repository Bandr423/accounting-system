def sales_list(request):
    sales = Sale.objects.all()
    return render(request, 'core/sales_list.html', {'sales': sales})

def add_sale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            sale = form.save()
            # تحديث الكمية في المخزون
            inventory = get_object_or_404(Inventory, product=sale.product)
            if inventory.quantity >= sale.quantity:
                inventory.quantity -= sale.quantity
                inventory.save()
            else:
                form.add_error(None, "الكمية المطلوبة غير متوفرة في المخزون.")
                return render(request, 'core/add_sale.html', {'form': form})
            return redirect('sales_list')
    else:
        form = SaleForm()
    return render(request, 'core/add_sale.html', {'form': form})
