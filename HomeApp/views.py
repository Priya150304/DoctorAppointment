from django.shortcuts import render
from django.http import HttpResponse
import pymongo

url = "mongodb://localhost:27017"
client = pymongo.MongoClient(url)
db =client['DemoDb']
demoCollection = db.DemoCollections

# Create your views here.

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def service(request):
    return render(request,'service.html')
def contact(request):
    return render(request,'contact.html')
def feature(request):
    return render(request,'feature.html')
def appointment(request):
    if request.method == 'POST':
        # Extract data from the form
        name = request.POST.get('app-name')
        email = request.POST.get('app-email')
        date = request.POST.get('app-date')
        time = request.POST.get('app-time')
        mobile = request.POST.get('app-mobile')
        doc = request.POST.get('app-doc')
        problem = request.POST.get('app-problem')
        
        doctor = { "name" : name, "email" : email, "date":date, "time":time, "mobile":mobile, "doctor":doc,"problem":problem}
        demoCollection.insert_one(doctor)
    return render(request,'appointment.html')
def team(request):
    return render(request,'team.html')
def testimonial(request):
    return render(request,'testimonial.html')
def err(request):
    return render(request,'err.html')
