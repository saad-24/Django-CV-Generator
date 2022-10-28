from unicodedata import name
from django.shortcuts import render,HttpResponse,HttpResponseRedirect, redirect
from Home.models import Top

# Create your views here.
def home(request):
    return render(request,"home.html")


def show(request):
    data = Top.objects.all()
    return render(request,"show.html",{'data':data})

def view(request,id):
    user_profile = Top.objects.get(pk=id)
    return render(request, "cv.html",{'user_profile':user_profile})


def send(request):
    if request.method == 'POST':
        name = request.POST['name']
        title = request.POST['title']
        phone = request.POST['phone']
        email = request.POST['email']
        linkedin_profile = request.POST['linkedin_profile']
        github_profile = request.POST['github_profile']
        portfolio_link = request.POST['portfolio_link']
        content = request.POST['content']

        tenure = request.POST['tenure']
        designation = request.POST['designation']
        company_name = request.POST['company_name']
        description = request.POST['description']

        tenure1 = request.POST['tenure1']
        designation1 = request.POST['designation1']
        company_name1 = request.POST['company_name1']
        description1 = request.POST['description1']

        tenure2 = request.POST['tenure2']
        designation2 = request.POST['designation2']
        company_name2 = request.POST['company_name2']
        description2 = request.POST['description2']

        period = request.POST['period']
        degree = request.POST['degree']
        institute_name = request.POST['institute_name']
        academic_details = request.POST['academic_details']
        skills = request.POST['skills']
        skills1 = request.POST['skills1']
        skills2 = request.POST['skills2']
        certificate_name = request.POST['certificate_name']
        certificate_name1 = request.POST['certificate_name1']
        certificate_name2 = request.POST['certificate_name2']
        Top(name = name,title=title,phone=phone,email=email,linkedin_profile=linkedin_profile,github_profile=github_profile,portfolio_link=portfolio_link,content=content,tenure=tenure,designation=designation,company_name=company_name,description=description,tenure1=tenure1,designation1=designation1,company_name1=company_name1,description1=description1,tenure2=tenure2,designation2=designation2,company_name2=company_name2,description2=description2,period=period,degree=degree,institute_name=institute_name,academic_details=academic_details,skills=skills,skills1=skills1,skills2=skills2,certificate_name=certificate_name,certificate_name1=certificate_name1,certificate_name2=certificate_name2).save()
        
        msg="CV created Successfully"
        return render(request,"home.html",{'msg':msg})
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")
    
def delete(request, id):
    data=Top.objects.get(pk=id)
    data.delete()
    return redirect('/show')

def edit(request, id):
    data=Top.objects.get(pk=id)
    return render(request,"edit.html", {'data':data})
   
def RecordEdited(request):
    if request.method == 'POST':
        name = request.POST['name']
        title = request.POST['title']
        phone = request.POST['phone']
        email = request.POST['email']
        linkedin_profile = request.POST['linkedin_profile']
        github_profile = request.POST['github_profile']
        portfolio_link = request.POST['portfolio_link']
        content = request.POST['content']

        tenure = request.POST['tenure']
        designation = request.POST['designation']
        company_name = request.POST['company_name']
        description = request.POST['description']

        tenure1 = request.POST['tenure1']
        designation1 = request.POST['designation1']
        company_name1 = request.POST['company_name1']
        description1 = request.POST['description1']

        tenure2 = request.POST['tenure2']
        designation2 = request.POST['designation2']
        company_name2 = request.POST['company_name2']
        description2 = request.POST['description2']

        period = request.POST['period']
        degree = request.POST['degree']
        institute_name = request.POST['institute_name']
        academic_details = request.POST['academic_details']
        skills = request.POST['skills']
        skills1 = request.POST['skills1']
        skills2 = request.POST['skills2']
        certificate_name = request.POST['certificate_name']
        certificate_name1 = request.POST['certificate_name1']
        certificate_name2 = request.POST['certificate_name2']

        Top.objects.filter(phone=phone).update(name = name,title=title,phone=phone,email=email,linkedin_profile=linkedin_profile,github_profile=github_profile,portfolio_link=portfolio_link,content=content,tenure=tenure,designation=designation,company_name=company_name,description=description,tenure1=tenure1,designation1=designation1,company_name1=company_name1,description1=description1,tenure2=tenure2,designation2=designation2,company_name2=company_name2,description2=description2,period=period,degree=degree,institute_name=institute_name,academic_details=academic_details,skills=skills,skills1=skills1,skills2=skills2,certificate_name=certificate_name,certificate_name1=certificate_name1,certificate_name2=certificate_name2)
        return HttpResponseRedirect("show")
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")




























