from django.shortcuts import render_to_response
from django.template import RequestContext
from images.models import Image
from django.contrib.auth.models import User
from images.forms import UploadImageForm
from django.http import Http404, HttpResponseRedirect, HttpResponse

def test_view(request):
    return render_to_response('images_test.html', RequestContext(request))

def upload_image(request):
    """
    Uploads an image from the form.
    """
    # Make sure you can only upload photos if you're logged in.
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')

    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = Image(
                user=request.user,
                image=request.FILES['image'],
                title=form.cleaned_data['title']
            )
            image.save()
            return HttpResponseRedirect('/')
    else:
        form = UploadImageForm()
    variables = RequestContext(request, {'form': form})
    return render_to_response('image_upload.html', variables)

def delete_image(request):
    """
    Deletes an image.
    """

def single_image(request, image_id):
    """
    Displays a single image.
    """

def all_portfolio_images(request, username):
    """
    Displays all images a user has uploaded to their portfolio.
    """
    user = User.objects.get(username=username)
    user_image_list = Image.objects.filter(user=user)
    variables = RequestContext(request, {
        'username': username,
        'image_list': user_image_list
    })
    return render_to_response('gallery.html', variables)
