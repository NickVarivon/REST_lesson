from django.contrib import admin

from api1.models import Category, Service, Salon, Person, Houses, Cities


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class SalonAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Salon, SalonAdmin)
admin.site.register(Person)
admin.site.register(Houses)
admin.site.register(Cities)

