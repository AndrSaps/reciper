# Generated by Django 3.0.10 on 2020-11-29 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reciper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cookcategories',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='static/images/categories/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cook_categories',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='recipe_cook_categories', to='reciper.CookCategories', verbose_name='Необхідно для приготування'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='static/images/recipes/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='serviseuser',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='static/images/users/', verbose_name='Фото'),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000, verbose_name='Текст')),
                ('author', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='reciper.ServiseUser')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reciper.Recipe', verbose_name='Коментар')),
            ],
        ),
    ]