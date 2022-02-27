from rest_framework.routers import DefaultRouter

from main.api.v1.views.manufactor import ManufactorView


from main.api.v1.views.contacts import ContactsView

from main.api.v1.views. about import AboutView
from main.api.v1.views.category import CategoryView
from main.api.v1.views.partner import PartnerView
from main.api.v1.views.product import ProductView

router = DefaultRouter()

router.register(r'manufactor', ManufactorView, basename='manufactor')
router.register(r'contacts', ContactsView, basename='contacts')

router.register(r'about', AboutView, basename='about')
router.register(r'category', CategoryView, basename='category')

router.register(r'partner', PartnerView, basename='partner')

router.register(r'product', ProductView, basename='product')


urlpatterns = router.urls