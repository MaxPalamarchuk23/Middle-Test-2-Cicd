from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.

class RecipeListView(ListView):
    model=Recipe
    template_name="admin_templates/product_list.html"
    paginate_by=3

    def get_queryset(self):
        filter_val=self.request.GET.get("filter","")
        order_by=self.request.GET.get("orderby","id")
        if filter_val!="":
            receipts=Recipe.objects.filter(Q(recipe_name__contains=filter_val) | Q(recipe_description__contains=filter_val)).order_by(order_by)
        else:
            receipts=Recipe.objects.all().order_by(order_by)
        
        recipe_list=[]
        for recipe in receipts:
            recipe_media=ProductMedia.objects.filter(recipe_id=recipe.id,is_active=1).first()
            recipe_list.append({"product":recipe})

        return recipe_list

 class RecipeDescriptionView(View):
    def get(self, request, recipe_id):
        recipe = get_object_or_404(Recipe, id=recipe_id)
        return render(request, 'recipe_description.html', {'recipe': recipe})
