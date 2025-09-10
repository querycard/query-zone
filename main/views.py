from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'npm' : '2406496063',
        'name': 'Khansa Dinda Arya Putri',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)