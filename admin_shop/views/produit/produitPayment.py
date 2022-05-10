from django.shortcuts import render
from django.views import View


class ProduitPaymentView(View):
    template_name = 'admin_shop/sites/product-payment.html'

    def get(self, request):
        return render(request, self.template_name)