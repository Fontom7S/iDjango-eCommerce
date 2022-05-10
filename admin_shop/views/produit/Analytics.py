from django.shortcuts import render
from django.views import View


class AnalyticsView(View):
    template_name = 'admin_shop/sites/analytics.html'

    def get(self, request):
        return render(request, self.template_name)