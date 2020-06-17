import functools
import ssl
from .models import MyModel

from django.conf import settings
from django.views.generic import DetailView

from django_weasyprint import WeasyTemplateResponseMixin,WeasyTemplateResponse
from django_weasyprint.views import CONTENT_TYPE_PNG
from django.utils import timezone

class MyModelView(DetailView):
    # vanilla Django DetailView
    model = MyModel
    template_name = 'builder/index.html'
    context_object_name = 'mod'

# class CustomWeasyTemplateResponse(WeasyTemplateResponse):
#     # customized response class to change the default URL fetcher
#     def get_url_fetcher(self):
#         # disable host and certificate check
#         context = ssl.create_default_context()
#         context.check_hostname = False
#         context.verify_mode = ssl.CERT_NONE
#         return functools.partial(django_url_fetcher, ssl_context=context)
#
# class MyModelPrintView(WeasyTemplateResponseMixin, MyModelView):
#     # output of MyModelView rendered as PDF with hardcoded CSS
#     pdf_stylesheets = [
#         settings.STATIC_DIR + 'css/resumestyles.css',
#     ]
#     # show pdf in-line (default: True, show download dialog)
#     pdf_attachment = False
#     # custom response class to configure url-fetcher
#     response_class = CustomWeasyTemplateResponse

class MyModelDownloadView(WeasyTemplateResponseMixin, MyModelView):
    # suggested filename (is required for attachment/download!)
    pdf_filename = 'foo.pdf'

# class MyModelImageView(WeasyTemplateResponseMixin, MyModelView):
#     # generate a PNG image instead
#     content_type = CONTENT_TYPE_PNG

    # dynamically generate filename
    # def get_pdf_filename(self):
    #     return 'foo-{at}.pdf'.format(
    #         at=timezone.now().strftime('%Y%m%d-%H%M'),
    #     )
