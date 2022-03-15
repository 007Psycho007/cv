from django.shortcuts import render
from .models import Skills, WorkExperiences, Education
from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas
import io
# Create your views here.
def index(request):
    profile = {"name": "Jan Peterhänsel",
               "job": "Python Developer",
               "home": "Wuerzburg, Bavaria, Germany",
               "mail": "info@janpeterhaensel.de"
               }
    skills_prog = Skills.objects.filter(category="programming").order_by("-proficency")
    skills_sys = Skills.objects.filter(category="sysadmin").order_by("-proficency")
    skills_other = Skills.objects.filter(category="other").order_by("-proficency")
    skills_languages = Skills.objects.filter(category="languages").order_by("-proficency")
    skills  = {"prog": skills_prog,"sys": skills_sys,"other":skills_other,"lang": skills_languages}
    work = WorkExperiences.objects.all().order_by('-time_begin')
    education = Education.objects.all().order_by('-time_begin')
    return render(request,'resume/index.html', {"profile": profile, "skills": skills, "work": work, "education": education})

# Not yet implemented
def download(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    return FileResponse