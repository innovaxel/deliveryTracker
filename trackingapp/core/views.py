""" This file contains the views for the core app. """

import secrets
import string
from django.shortcuts import render
from .models import OrderTrack

# Create your views here.


def generate_trackingId():
    """
    This function is used to generate a tracking id for the order
    """
    tracking_id = "".join(
        secrets.choice(string.ascii_uppercase + string.digits) for _ in range(8)
    )
    return tracking_id


def add_order(request):
    """
    This view is used to add an order to the database
    """
    if request.method == "POST":
        order_date = request.POST.get("order_date")
        sender_name = request.POST.get("sender_name")
        sender_address = request.POST.get("sender_address")
        receiver_name = request.POST.get("receiver_name")
        receiver_address = request.POST.get("receiver_address")
        receiver_email = request.POST.get("receiver_email")
        receiver_phone = request.POST.get("receiver_phone")
        tracking_id = generate_trackingId()
        order = OrderTrack(
            order_date=order_date,
            sender_name=sender_name,
            sender_address=sender_address,
            receiver_name=receiver_name,
            receiver_address=receiver_address,
            receiver_email=receiver_email,
            receiver_phone=receiver_phone,
            tracking_id=tracking_id,
        )
        order.save()
        return render(request, "addOrder.html", {"order_submitted": True})
    return render(request, "addOrder.html", {"order_submitted": False})



def search_order(request):
    """
    This view is used to search for an order in the database
    """
    if request.method == "POST":
        tracking_id = request.POST.get("tracking_id")
        order = OrderTrack.objects.filter(tracking_id=tracking_id)
        return render(request, "searchOrder.html", {"order": order})
    return render(request, "searchOrder.html")
