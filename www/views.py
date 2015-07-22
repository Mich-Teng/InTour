from django.shortcuts import render_to_response


# home page view of InTour
def homepage_view(request):
    return render_to_response("homepage.html", {})
