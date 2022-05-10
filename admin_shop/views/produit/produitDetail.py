from django.shortcuts import render
from django.views import View


class ProduitDetailView(View):
    template_name = 'admin_shop/sites/product-detail.html'

    def get(self, request):
        return render(request, self.template_name)