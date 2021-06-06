from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.contrib.auth.models import Group



from reciper.forms import CommentForm, ServiceUserForm, UserForm
from reciper.models import Recipe, ServiseUser

class RegisterView(View):
    def get(self,request):
        context = RequestContext(request)
        registered = False
        user_form = UserForm()
        service_user_form = ServiceUserForm()
        return render(request,'registration/register.html',
                      {'user_form': user_form, 'service_user_form': service_user_form, 'registered': registered})

    def post(self,request):
        context = RequestContext(request)
        registered = False
        user_form = UserForm(data=request.POST)
        service_user_form = ServiceUserForm(data=request.POST)

        if user_form.is_valid() and service_user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            user.is_staff = True
            my_group = Group.objects.get(name='Стафф')
            user.set_password(user.password)
            user.save()
            my_group.user_set.add(user)
            my_group.save()
            profile = service_user_form.save(commit=False)
            profile.user = user
            if 'photo' in request.FILES:
                profile.photo = request.FILES['photo']
            profile.save()
            registered = True

        else:
            print(user_form.errors, service_user_form.errors)
        return redirect('/')



def logout_view(request):
    logout(request)
    redirect('/')
    # Redirect to a success page.


class RecipeView(ListView):
    model = Recipe
    queryset = Recipe.objects.all()
    template_name = 'recipe_list.html'

class Report(View):
    def get(self,request):
        recipes = Recipe.objects.all()
        users = ServiseUser.objects.all()
        return render(request,'report.html', {'recipes':recipes,"users":users})


class RecipeDetailView(DetailView):
    model = Recipe
    slug_field = 'id'
    template_name = 'recipe_detail.html'

class AddReview(View):
    def get(self,request,pk):
        recipe = Recipe.objects.get(id = pk)
        recipe.reviews += 1
        recipe.save()
        return redirect("/"+str(pk))

class SaveRecipe(View):
    def post(self,request,pk,usr_id):
        user = ServiseUser.objects.get(id = usr_id)
        recipe = Recipe.objects.get(id = pk)
        if recipe not in user.saved_recipes.all():
            user.saved_recipes.add(recipe)
        else:
            user.saved_recipes.remove(recipe)
        user.save()
        return redirect("/"+str(pk))


class AddComment(View):
    def post(self,request,pk,usr_id):
        form =  CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.recipe_id = pk
            form.author_id = usr_id
            form.save()
        return redirect("/"+str(pk)+"/#comments")


class SavedView(View):
    def get(self,request,pk):
        user = ServiseUser.objects.get(id=pk)
        recipes = user.saved_recipes.all()
        return render(request,'saved.html', {'recipe_list':recipes})

class ShowOwn(View):
    def get(self,request,pk):
        return redirect("/admin/reciper/serviseuser/"+str(pk)+"/change/")