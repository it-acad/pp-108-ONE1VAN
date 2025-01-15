from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'created_at', 'plated_end_at', 'end_at', 'status') 
    list_filter = ('book', 'user')  
    search_fields = ('user__username', 'book__name')  
    ordering = ('-created_at',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset

    def status(self, obj):
        return "Returned" if obj.end_at else "Not Returned"
    status.short_description = 'Status'

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

admin.site.register(Order, OrderAdmin)
