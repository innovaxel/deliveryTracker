""" This file contains the views for the core app. """

import secrets
import string
from django.shortcuts import render
from .models import OrderTrack

from trackingapp.settings import *
from .utils import send_email

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
        print("here")
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

        subject = "Your Order has been placed"
        email_body = f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: 'Arial', sans-serif;
                    font-size: 16px;
                    color: #333;
                    margin: 0;
                    padding: 0;
                    background-color: #f5f5f5;
                }}
                .container {{
                    max-width: 600px;
                    margin: 20px auto;
                    padding: 20px;
                    background-color: #fff;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    border-radius: 8px;
                }}
                h1 {{
                    color: #002600;
                    font-size: 24px;
                }}
                h2 {{
                    color: #333;
                    font-size: 20px;
                }}
                p {{
                    margin: 10px 0;
                    line-height: 1.6;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Your Order has been placed.</h1>
                <h2>Your Tracking Id: {tracking_id}</h2>
                <p>Please visit this link to track your order: <a href="https://pilotdelivery.ne" style="color: #1e90ff;">pilotdelivery.ne</a></p>
                <p>Have a Great Day.</p>
                <p>Best Regards,<br>Team PILOT</p>
            </div>
        </body>
        </html>
        """


        sender = EMAIL_HOST_USER
        recipients = [receiver_email]
        password = EMAIL_HOST_PASSWORD
        send_email(subject, email_body, sender, recipients, password)
        return render(request, "addOrder.html", {"order_submitted": True})
    return render(request, "addOrder.html", {"order_submitted": False})



def search_order(request):
    """
    This view is used to search for an order in the database
    """
    if request.method == "POST":
        # get the tracking id from the form
        data = request.POST
        tracking_id = data["tracking_id"]
        print("tracking_id", tracking_id)

        order = OrderTrack.objects.filter(tracking_id=tracking_id)
        print("order", order)
        return render(request, "searchOrder.html", {"order": order, "tracking_id": tracking_id})

    return render(request, "searchOrder.html")
