import os

import stripe
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Payment
from .serializers import PaymentSerializer


class CreateStripePaymentIntentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        payment = serializer.save(student=request.user)

        secret_key = os.getenv("STRIPE_SECRET_KEY", "")
        if not secret_key:
            return Response(
                {
                    "payment": PaymentSerializer(payment).data,
                    "detail": "Stripe key not configured. Add STRIPE_SECRET_KEY to enable live payments.",
                },
                status=status.HTTP_201_CREATED,
            )

        stripe.api_key = secret_key
        intent = stripe.PaymentIntent.create(
            amount=int(float(payment.amount) * 100),
            currency=payment.currency.lower(),
            metadata={"payment_id": str(payment.id), "user_id": str(request.user.id)},
        )
        payment.provider_payment_id = intent.id
        payment.save(update_fields=["provider_payment_id"])

        return Response(
            {
                "payment": PaymentSerializer(payment).data,
                "client_secret": intent.client_secret,
                "publishable_key": os.getenv("STRIPE_PUBLISHABLE_KEY", ""),
            },
            status=status.HTTP_201_CREATED,
        )
