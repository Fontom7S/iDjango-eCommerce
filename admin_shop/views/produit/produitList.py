from django.shortcuts import render
from django.views import View


class ProduitListView(View):
    template_name = 'admin_shop/sites/product-list.html'

    def get(self, request):
        return render(request, self.template_name)