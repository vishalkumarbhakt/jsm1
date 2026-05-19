from django.urls import path

from .views import CreateStripePaymentIntentView

urlpatterns = [
    path("create-intent/", CreateStripePaymentIntentView.as_view(), name="create-payment-intent"),
]
