from django.shortcuts import render
from django.views import View


class ProduitEditView(View):
    template_name = 'admin_shop/sites/product-edit.html'

    def get(self, request):
        return render(request, self.template_name)