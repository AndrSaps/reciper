from django.contrib import admin

from .models import Product,ServiseUser,Categories,CookCategories,Step,Recipe,Comments
# Register your models here.

admin.site.site_header = 'Reciper'

class RecipeInline(admin.TabularInline):
    model = Recipe
    fk_name="author"
    extra = 1
    fields = ("id","title","description","reviews",)
    readonly_fields = ("reviews",)
    show_change_link = ("id","title","description","reviews",)


class ProductsInline(admin.TabularInline):
    model = Product
    extra = 1

class StepInline(admin.TabularInline):
    model = Step
    extra = 3

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "reviews")
    inlines = [ProductsInline,StepInline]
    readonly_fields = ("reviews","publishDate","severs")

@admin.register(ServiseUser)
class ServiceUserAdmin(admin.ModelAdmin):
    list_display = ("id", "photo")
    inlines = [RecipeInline]
    save_on_top = True
    readonly_fields = ("user",)
    

admin.site.register(Product)
admin.site.register(Comments)
admin.site.register(Categories)
admin.site.register(CookCategories)
admin.site.register(Step)