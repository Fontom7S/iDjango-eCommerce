from django.shortcuts import render
from django.views import View


class WidgetsView(View):
    template_name = 'admin_shop/sites/widgets.html'

    def get(self, request):
        return render(request, self.template_name)