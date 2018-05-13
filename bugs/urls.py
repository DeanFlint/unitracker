from django.conf.urls import url, include
from .views import view_bugs
# from .views import view_cart, add_to_cart, adjust_cart

urlpatterns = [
    url(r'^$', view_bugs, name='view_bugs')
    ]