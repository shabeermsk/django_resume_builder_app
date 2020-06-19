# import uuid
from django.db import models
from django.utils import timezone
# from django.contrib import auth
from django.urls import reverse
from django.template.defaultfilters import slugify
from tinymce.models import HTMLField


class ResumeTemplate(models.Model):
    # thumbnail = models.ImageField(upload_to=resume_thumb)
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    content = models.TextField()
    name_o = models.TextField(blank=True)
    name_c = models.TextField(blank=True)
    email_o = models.TextField(blank=True)
    email_c = models.TextField(blank=True)
    phone_o = models.TextField(blank=True)
    phone_c = models.TextField(blank=True)
    education_o = models.TextField(blank=True)
    education_c = models.TextField(blank=True)
    experience_o = models.TextField(blank=True)
    experience_c = models.TextField(blank=True)
    skills_o = models.TextField(blank=True)
    skills_c = models.TextField(blank=True)
    father_o = models.TextField(blank=True)
    father_c = models.TextField(blank=True)
    mother_o = models.TextField(blank=True)
    mother_c = models.TextField(blank=True)
    dob_o = models.TextField(blank=True)
    dob_c = models.TextField(blank=True)
    intrest_o = models.TextField(blank=True)
    intrest_c = models.TextField(blank=True)
    address_o = models.TextField(blank=True)
    address_c = models.TextField(blank=True)
    declaration_o = models.TextField(blank=True)
    declaration_c = models.TextField(blank=True)

    # slug = models.SlugField(null=False,unique=True)
    posted_date = models.DateTimeField(auto_now=True)

    class Meta:
       ordering = ('-posted_date', )

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
        # return reverse('',kwargs={'slug':self.slug})

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.name)
    #     return super().save(*args, **kwargs)


class Resume(models.Model):

    template = models.ForeignKey(ResumeTemplate,related_name='resumetemplate',on_delete=models.CASCADE)
    slug = models.SlugField(null=False,unique=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    education = models.TextField(max_length=300)
    experience = models.TextField(max_length=400)
    skills = models.TextField(max_length=400)
    father = models.CharField(max_length=100)
    mother = models.CharField(max_length=100)
    dob = models.CharField(max_length=20)
    intrest = models.CharField(max_length=200)
    address = models.TextField(max_length=200)
    declaration = models.TextField(max_length=400)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('resumedwnbtn',kwargs={'slug':self.slug,'pk':self.template.pk})
