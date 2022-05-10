from django.shortcuts import render
from django.views import View


class ProduitCartView(View):
    template_name = 'admin_shop/sites/product-cart.html'

    def get(self, request):
        return render(request, self.template_name)