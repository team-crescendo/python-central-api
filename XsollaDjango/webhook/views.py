from hashlib import sha1
from json import loads

from django.http import HttpResponse
from django.views.generic import View
from secret.secret import get_secret

SECRET_KEY = str.encode(get_secret("XSOLLA_SECRET_KEY"))


def is_authorized(request):
    signature = sha1(request.body + SECRET_KEY).hexdigest()
    return request.META.get('HTTP_AUTHORIZATION') == f"Signature {signature}"


class WebhookView(View):
    def post(self, request, *args, **kwargs):
        if not is_authorized(request):
            return HttpResponse(status=401)

        return HttpResponse(status=204)
