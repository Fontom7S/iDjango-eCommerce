from django.conf.urls.static import static
from django.urls import path

from admin_shop.views.dashbord import DashbordView
from admin_shop.views.produit.Analytics import AnalyticsView
from admin_shop.views.produit.produitCart import ProduitCartView
from admin_shop.views.produit.produitDetail import ProduitDetailView
from admin_shop.views.produit.produitList import ProduitListView
from admin_shop.views.produit.produitEdit import ProduitEditView
from admin_shop.views.produit.produitPayment import ProduitPaymentView
from admin_shop.views.produit.widgets import WidgetsView
from eCommerce import settings

app_name = 'admin_shop.py'
urlpatterns = [

    # url pour le site
    path(
        route='dashbord',
        view=DashbordView.as_view(),
        name='dashbord'
    ),
    # url pour les produits
    path(
            route='produitList',
            view=ProduitListView.as_view(),
            name='admin_produitList'
        ),
    path(
        route='produitEdit',
        view=ProduitEditView.as_view(),
        name='admin_produitEdit'
    ),
    path(
            route='produitDetail',
            view=ProduitDetailView.as_view(),
            name='admin_produitDetail'
        ),
    path(
            route='produitCart',
            view=ProduitCartView.as_view(),
            name='admin_produitCart'
        ),
    path(
            route='produitPayment',
            view=ProduitPaymentView.as_view(),
            name='admin_produitPayment'
        ),
    path(
        route='widgets',
        view=WidgetsView.as_view(),
        name='admin_widgets'
    ),
    path(
        route='analytics',
        view=AnalyticsView.as_view(),
        name='admin_analytics'
    ),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
