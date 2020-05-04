from django.shortcuts import render

# see urls.py
# each method correlates with a url
# index == '' name='listings',
# listing == '<id>' name="listing",
# search == 'search' name='search'
def index(request):
    return render(request, 'listings/listings.html')

def listing(request):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')
