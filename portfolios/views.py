from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from portfolios.forms import RegistrationForm
import json

def main_page(request):
    """
    Main page.
    """

    return render_to_response('main_page.html', RequestContext(request))

def user_page(request, username):
    """
    User's page.
    """

    try:
        user = User.objects.get(username=username)
    except:
        raise Http404('User name not found.')
    variables = RequestContext(request, {'username': username})
    return render_to_response('user_page.html', variables)

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            # Now, populate the profile from the form.
            profile = user.get_profile()
            profile.latitude = form.cleaned_data['latitude']
            profile.longitude = form.cleaned_data['longitude']
            profile.save()
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {'form': form})
    return render_to_response('registration/register.html', variables)

# Returns a list of all user's usernames.
def list_users(request):
    all_users = User.objects.all()
    result = []
    if all_users.count() < 1:
        result.append('No users found')
    else:
        for user in all_users:
            result.append(user.username)
    # Convert the response to JSON.
    return HttpResponse(json.dumps(result))

# Test views follow:
def xhr_test(request):
    if request.is_ajax():
        if request.method == 'GET':
            message = 'This is an XHR GET request'
        elif request.method == 'POST':
            message = 'This is an XHR POST request'
            # can access the POST data here
            print request.POST
    else:
        message = 'This is not an XHR request'
    return HttpResponse(message)
