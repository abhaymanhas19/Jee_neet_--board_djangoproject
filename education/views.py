from django.shortcuts import render, redirect
from .models import (
    Section,
    HistoricalData,
    ContactUs,
    Course,
    FAQ,
    StaffDetail,
    Testimonial,
    SiteLogo
)
from django.conf import settings
from django.http import HttpResponseNotFound


from django.http import HttpResponse
from education.models import ContactUs, Lead, SampleVideo

from django.views.decorators.csrf import csrf_exempt


def home(request, page_id):
    if page_id not in settings.ALLOWED_URL_OPTIONS:
        return HttpResponseNotFound("Not Found")
    context = {
        "historical_data": HistoricalData.objects.filter(page_id=page_id),
        "courses": Course.objects.filter(page_id=page_id),
        "faq": FAQ.objects.filter(page_id=page_id),
        "staff_details": StaffDetail.objects.filter(page_id=page_id),
        "testimonials": Testimonial.objects.filter(page_id=page_id),
        "samplevideos": SampleVideo.objects.filter(page_id=page_id),
        "page_id": page_id,
        "logos": SiteLogo.objects.filter(page_id=page_id),

    }
    return render(request, "index.html", context=context)


@csrf_exempt
def conatacus(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("number")
        user_type = request.POST.get("user_type")
        message = request.POST.get("message")
        ContactUs.objects.create(
            name=name, email=email, phone=number, type=user_type, message=message
        )
        return redirect("/thankyou")

@csrf_exempt
def userlead(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("number")

        Lead.objects.create(name=name, email=email, phone=number)
        return redirect("/thankyou")



def thankyoupage(request):
    return render(request, "thankyou.html")
