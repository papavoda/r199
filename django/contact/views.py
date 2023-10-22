from django.core.mail import EmailMessage, get_connection
from django.conf import settings
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic import TemplateView, View
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

from .forms import ContactUsForm
from .models import *


def send_email(request):
    messageSent = ''
    recipient_list = ''
    sender = ''
    if request.method == "POST":
        with get_connection(
                host=settings.EMAIL_HOST,
                port=settings.EMAIL_PORT,
                username=settings.EMAIL_HOST_USER,
                password=settings.EMAIL_HOST_PASSWORD,
                use_tls=settings.EMAIL_USE_TLS
        ) as connection:
            name = request.POST.get("name")
            phone = request.POST.get("phone")
            subject = request.POST.get("subject")
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [settings.EMAIL_TO, ]
            message = request.POST.get("message")
            feedback = f'{name} - {phone} - {subject}'
            EmailMessage(feedback, message, email_from, recipient_list, connection=connection).send()

        messageSent = True
        sender = name
    return render(request, 'about.html', {
        'recipient': recipient_list,
        'messageSent': messageSent,
        'sender': sender,
    })


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactUsForm
        context['about'] = About.objects.last()  # последний объект модели
        context['nbar'] = 'about'
        context['contact_links'] = ContactLink.objects.all()
        context['main_title'] = 'о нас'
        return context


class ContactUs(CreateView):
    model = ContactUs
    form_class = ContactUsForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.object = form.save()
            return send_email(request)
        else:
            context = {'form': form}
            # return redirect(reverse('cust_req'))
            return render(request, 'about.html', context)

# class SmallPromoAboutView(View):
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context
