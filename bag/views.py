from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """
    render bag view
    """
    return render(request, 'bag/bag.html')
