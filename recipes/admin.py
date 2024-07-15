from django.contrib import admin
from .models import Category, Recipe


class CaregoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CaregoryAdmin)
