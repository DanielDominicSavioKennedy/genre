from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .metadata import getdata
from .predict import predict_genre
# Create your views here.

def main(request):
    return HttpResponse("Hello")

def home(request):
    if request.method == 'POST':
        uploadfile = request.FILES['document']
        #print(uploadfile.name)
        #print(uploadfile.size)
        if not uploadfile.name.endswith('.wav'):
            messages.error(request,'Only .wav file type is allowed')
            return redirect(home)
        meta = getdata(uploadfile)
        pred=predict_genre(meta)
        return render(request,'result.html',{"result":pred})
    else:
        return render(request,'base.html')

