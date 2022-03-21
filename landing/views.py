from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ContactForm
from .models import Option
from django.contrib import messages  # using flash messages
# used for reCaptcha verifying at server side
import urllib.request
import json
from django.conf import settings


# Create your views here.
def index(req):
    result = False  # default value

    if req.method == "POST":
        form = ContactForm(req.POST)
        if form.is_valid():
            ''' Begin reCAPTCHA validation '''
            recaptcha_response = req.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            captcha_req = urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(captcha_req)
            captcha_result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''

            if captcha_result['success']:
                # sending information from contact form to system email
                # gmail
                result = SendingEmail(
                    form.cleaned_data["contact_name"],
                    form.cleaned_data["contact_email"],
                    form.cleaned_data["contact_message"],
                    form.cleaned_data["contact_phone"],
                    )
            else:
                result = False
        else:
            result = False

        if result:
            messages.add_message(req, messages.SUCCESS,
                                 'Cảm ơn bạn đã gởi tin nhắn liên hệ với HoadonAZ.'
                                 )
            form = ContactForm()  # reset form
        else:
            messages.add_message(
                req, messages.ERROR, 'Thông tin liên hệ gởi đi không thành công.<br/>Vui lòng kiểm tra lại thông tin nhập vào hoặc hãy thử liên hệ bằng phương thức khác.'
                )

    else:
        form = ContactForm()

    context_for_view = {
        'contact_form': form,
        'canonical': req.build_absolute_uri(req.path)
    }

    return render(req, 'landing/index.html', context_for_view)


def page404(req):
    return HttpResponseRedirect(reverse("landing:landing"))


def SendingEmail(form_name, form_email, form_msg, form_phone=''):
    to_email = Option.objects.get(name='sysemail').value
    results = send_mail(
        "Contact from {} - {} - {}".format(form_name, form_phone, form_email),
        form_msg,
        to_email,
        # sending mail to myself
        [to_email],
        fail_silently=False,
    )

    if results > 0:
        return True
    else:
        return False
