from .models import Inventory, Sale, Purchase

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'low_stock_threshold', 'last_updated')
    search_fields = ('product__name',)
    list_filter = ('last_updated',)

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'sale_price', 'date')
    search_fields = ('product__name',)
    list_filter = ('date',)

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'purchase_price', 'date')
    search_fields = ('product__name',)
    list_filter = ('date',)

    class Inventory(models.Model):
        product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="inventory")
        quantity = models.IntegerField(default=0)
        low_stock_threshold = models.IntegerField(default=5)  # تحذير عند انخفاض المخزون
        last_updated = models.DateTimeField(auto_now=True)

        def is_low_stock(self):
            return self.quantity <= self.low_stock_threshold

        def __str__(self):
            return f"{self.product.name} - {self.quantity}"