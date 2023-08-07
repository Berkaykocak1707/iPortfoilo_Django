from django.contrib import admin
from .models import Profile, Resume, Category, Portfolio, PortfolioPhoto
from django.utils.text import slugify

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'degree', 'email']

class ResumeAdmin(admin.ModelAdmin):
    list_display = ['resume_type', 'name', 'years']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.name)
        super().save_model(request, obj, form, change)

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title', 'name', 'client', 'date', 'address',]
    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.title)
        super().save_model(request, obj, form, change)

class PortfolioPhotoAdmin(admin.ModelAdmin):
    list_display = ['portfolio']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Resume, ResumeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(PortfolioPhoto, PortfolioPhotoAdmin)
