from celery import Celery, shared_task
from rest_framework import request
from RMS_Tenant import settings

from reservation.models import Reservation
from django.core.mail import send_mail
from decouple import config

from django_tenants.utils import schema_context
import logging

logger = logging.getLogger(__name__)


@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    retry_kwargs={
        "max_retries": 5,
        "countdown": 1 * 60,
    },  # retry up to 2 times with 1 minutes between retries)
)
def send_reservation_email(self, reservation_id, schema_name):
    print("TRiggered the task to send email")

    try:
        with schema_context(schema_name):
            reservation = Reservation.objects.get(id=reservation_id)
            tenant_name = schema_name
            logger.info(f"Trying to send email to -->{reservation.user.email}  ")
            send_mail(
                subject=f"Reservation at {tenant_name}",
                message="Thank you for your reservation.",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[reservation.user.email],
            )
            logger.info(
                f"{reservation.user.email} has received email after reserving the table. "
            )
    except Exception as e:
        logger.error(f"Failed to send reservation email: {e}")
