from django import forms
from images.models import Image

# Form created from Image model for uploading images.
class UploadImageForm(forms.Form):
    image = forms.ImageField(label='Upload an image')
    title = forms.CharField(label='Title')

    def clean_image(self):
        image = self.cleaned_data['image']
        if image:
            if image._size > 1*1024*1024:
                raise forms.ValidationError('Image is too large')
            return image
        else:
            raise forms.ValidationError('Image upload failed')
