from django.contrib import admin
from .models import Borrow, Department, Peripheral, Category


class BorrowAdmin(admin.ModelAdmin):
    list_display = ("borrow_id", "borrower_name", "department", "category","peripheral", "unique_number")
    list_filter = ("status",)
    search_fields = ("borrower_name", "department__department_description")

admin.site.register(Borrow, BorrowAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("department_id", "department_description", "status")
    list_filter = ("status",)
    search_fields = ("department_description",)


admin.site.register(Department, DepartmentAdmin)


class PeripheralAdmin(admin.ModelAdmin):
    list_display = ("peripheral_id", "peripheral_description", "unique_number","status")
    list_filter = ("status",)
    search_fields = ("peripheral_description", "unique_number")


admin.site.register(Peripheral, PeripheralAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_id", "category_description")
    search_fields = ("category_description",)


admin.site.register(Category, CategoryAdmin)