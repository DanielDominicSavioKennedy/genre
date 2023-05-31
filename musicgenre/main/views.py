from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .metadata import getdata
# Create your views here.

def main(request):
    return HttpResponse("Hello")

def home(request):
    if request.method == 'POST':
        uploadfile = request.FILES['document']
        print(uploadfile.name)
        print(uploadfile.size)
        if not uploadfile.name.endswith('.wav'):
            messages.error(request,'Only .wav file type is allowed')
            return redirect(home)
        meta = getdata(uploadfile)
        print(meta)
    return render(request,'base.html')

