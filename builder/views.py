import functools
# import ssl
from django.shortcuts import render
from .models import Resume,ResumeTemplate
from django.template.loader import get_template,render_to_string
from django.conf import settings
from django.views.generic import DetailView,ListView,CreateView

from django_weasyprint import WeasyTemplateResponseMixin,WeasyTemplateResponse
# from django_weasyprint.views import CONTENT_TYPE_PNG
from django.utils import timezone
from braces.views import SelectRelatedMixin


class IndexListView(ListView):
    model = ResumeTemplate
    template_name = 'builder/index.html'
    context_object_name = 'resumetemplate'


class ResumeTemplateDetailView(DetailView):
    model = ResumeTemplate
    template_name = 'builder/resumedetail.html'
    context_object_name = 'resumetemplate'


class ResumeCreateView(SelectRelatedMixin,CreateView):
    model = Resume
    # select_related = ['resumetemplate']
    template_name = 'builder/resume_form.html'
    fields = ['name','email','phone','education','experience','skills','father','mother','dob','intrest','address','declaration']
    # success_url = 'resumedwnbtn'

    def form_valid(self, form):
        form.instance.template = ResumeTemplate.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)
    # redirect_field_name = 'builder/resumedwnbtn.html'

class ResumeReadyView(DetailView):
    # vanilla Django DetailView
    model = Resume
    template_name = 'builder/resumedwnbtn.html'
    # def get_context_data(self, **kwargs):
    #     context = super(ResumeReadyView, self).get_context_data(**kwargs)
    #     context = self.get_document(context)
    #     return context
    #
    # def get_document(self, context):
    #     data = render_to_string('resume_detail.html', context)
    #     return data

    # template = template.render()

    # context_object_name = 'resume'

    # def get(self,context):
    #     return render(template,context)


class FinalResumeView(DetailView):
    model = Resume
    template_name = 'builder/finalresume.html'
    context_object_name = 'resume'

class DownloadView(WeasyTemplateResponseMixin, FinalResumeView):
    # suggested filename (is required for attachment/download!)
    # pdf_filename = 'foo.pdf'

    # dynamically generate filename
    def get_pdf_filename(self):
        return 'resume-builder-{at}.pdf'.format(
            at=timezone.now().strftime('%Y%m%d-%H%M'),
        )
