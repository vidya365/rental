from django.contrib import admin
from django.utils.html import format_html
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import path, reverse
from .models import RentalItem, RentalRequest, Payment, UserDetail
from .utils import generate_receipt

@admin.register(RentalItem)
class RentalItemAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'price_per_day',
        'available_quantity',
        'stock_status',
        'available',
        'next_available_date',
    )
    search_fields = ('title',)
    list_filter = ('available',)
    fields = (
        'title',
        'description',
        'price_per_day',
        'available_quantity',
        'deposit',
        'next_available_date',
        'image',
    )

    def stock_status(self, obj):
        if obj.available_quantity == 0:
            return "Sold Out"
        elif obj.available_quantity == 1:
            return "Only 1 Left"
        else:
            return f"{obj.available_quantity} Available"
    stock_status.short_description = "Stock Status"

@admin.register(RentalRequest)
class RentalRequestAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'rental_item',
        'start_date',
        'end_date',
        'get_rental_days',    
        'get_per_day_rent',   
        'status',
        'total_amount',
        'is_reminder_sent',
        'is_overdue_email_sent',
        'order_id',
        'deposit',
        'download_receipt',
    )
    list_filter = ('status', 'payment_method', 'start_date', 'end_date')
    search_fields = ('user__username', 'rental_item__title')

    def get_rental_days(self, obj):
        return obj.rental_days
    get_rental_days.short_description = "Days"

    def get_per_day_rent(self, obj):
        value = obj.per_day_rent
        return f"₹{value}" if value else "—"
    get_per_day_rent.short_description = 'Per Day Rent'

    def download_receipt(self, obj):
        if obj.receipt:
            url = reverse("admin:download_receipt", args=[obj.pk])
            return format_html('<a class="button" href="{}" target="_blank">Download PDF</a>', url)
        return "—"
    download_receipt.short_description = "Receipt"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                'download-receipt/<int:pk>/',
                self.admin_site.admin_view(self.generate_receipt_view),
                name="download_receipt",
            ),
        ]
        return custom_urls + urls

    def generate_receipt_view(self, request, pk, *args, **kwargs):
        try:
            order = RentalRequest.objects.get(pk=pk)
        except RentalRequest.DoesNotExist:
            self.message_user(request, "Order not found.", level='error')
            return HttpResponseRedirect(reverse('admin:rentalrequest_changelist'))

        if order and order.receipt:
            response = HttpResponse(order.receipt, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{order.receipt.name}"'
            return response
        else:
            # Generate live if not exists (optional fallback):
            pdf_file = generate_receipt(order)
            response = HttpResponse(pdf_file, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="receipt_{order.order_id}.pdf"'
            return response


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'rental_request',
        'payment_id',
        'order_id',
        'payment_status',
        'payment_date',
    )
    search_fields = (
        'payment_id',
        'order_id',
        'rental_request__user__username',
    )
    list_filter = ('payment_status', 'payment_date')

@admin.register(UserDetail)
class UserDetailAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'aadhar', 'city', 'state', 'pincode')
    search_fields = ('user__username', 'phone', 'aadhar', 'city', 'state')
    list_filter = ('state',)
    fields = (
        'user',
        'phone',
        'address_line1',
        'city',
        'state',
        'pincode',
        'aadhar',
        'email',
    )


from django.contrib import admin
from .models import Services

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'contact_number')
