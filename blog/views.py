from django.shortcuts import render

# Create your views here.
from django.shortcuts import  redirect
from .models import Info
from .forms import InfoForm

def info_list(request):
    infos = Info.objects.all()
    return render(request, 'blog/info_list.html', {'infos': infos})

def create_info(request):
    if request.method == 'POST':
        form = InfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('info_list')
    else:

        form = InfoForm()

        return render(request, 'blog/create_info.html', {'form': form})