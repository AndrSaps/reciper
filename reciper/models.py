from datetime import date

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CookCategories(models.Model):
    name = models.CharField("Назва", max_length=50)
    photo = models.ImageField("Фото",upload_to="static/images/categories/",default=None, blank=True, null=True)
    def __str__(self):
        return self.name

class Categories(models.Model):
    name = models.CharField("Назва", max_length=50)
    def __str__(self):
        return self.name

class ServiseUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField("Фото",upload_to="static/images/users/",default=None, blank=True, null=True)
    def __str__(self):
        return self.user.username

class Recipe(models.Model):
    title = models.CharField("Назва", max_length=100)
    reviews = models.PositiveIntegerField("Кількість переглядів",default=0)
    description = models.TextField("Опис", max_length=500)
    photo = models.ImageField("Фото", upload_to="static/images/recipes/",default=None, blank=True, null=True)
    publishDate = models.DateField("Дата опублікування",default=date.today)
    isValid = models.BooleanField("Чи відповідає стандартам",default=False)
    author = models.ForeignKey(ServiseUser, verbose_name="Автор", related_name="own_recipes",default=None, blank=True, null=True, on_delete=models.CASCADE)
    severs = models.ManyToManyField(ServiseUser, verbose_name="Зберегли", related_name="saved_recipes",default=None, blank=True, null=True)
    requiredTime = models.DurationField("Тривалість приготування",default=None, blank=True, null=True)
    cook_categories = models.ManyToManyField(CookCategories, verbose_name="Необхідно для приготування", related_name="recipe_cook_categories",default=None, blank=True, null=True)
    categories = models.ManyToManyField(Categories, verbose_name="Категорії", related_name="recipe_categories", default=None, blank=True, null=True)
    def __str__(self):
        return self.title



class Comments(models.Model):
    text = models.TextField("Текст", max_length=1000)
    author = models.ForeignKey(ServiseUser, on_delete=models.CASCADE, default=None, blank=True, null=True )
    recipe = models.ForeignKey(Recipe, verbose_name="Коментар", on_delete=models.CASCADE)
    def __str__(self):
        return self.author.user.username + " сказав " + self.text



class Product(models.Model):
    label = models.CharField("Назва", max_length=50)
    value = models.FloatField("Значення")
    measure = models.CharField("Міра", max_length=50)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name="Рецепт")
    def __str__(self):
        return self.label

class Step(models.Model):
    title = models.CharField("Заголовок", max_length=50)
    description = models.CharField("Опис", max_length=300)
    order = models.PositiveSmallIntegerField("Порядок")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name="Рецепт")
    def __str__(self):
        return self.title

