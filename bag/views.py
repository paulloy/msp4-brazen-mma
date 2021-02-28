from django.shortcuts import render


def view_bag(request):
    """ A view to return the bag template """

    return render(request, 'bag/bag.html')
