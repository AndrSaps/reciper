from rest_framework import serializers
from .models import Product,ServiseUser,Categories,CookCategories,Step,Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'