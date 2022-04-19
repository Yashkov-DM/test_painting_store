from django.shortcuts import render
from .forms import StoreForm


def index(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            form.save()

    form = StoreForm()
    data = {'form': form}
    return render(request, 'frontend/index.html', data)


