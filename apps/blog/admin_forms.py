from django import forms
from blog.models import Post
from django.core.exceptions import ValidationError


class PostAdminForm(forms.ModelForm):
    max_single_message = 1024
    max_message_with_image = 256

    def clean_message(self):
        import pdb
        pdb.set_trace()
        if self.cleaned_data.get('image'):
            if len(self.cleaned_data['message']) > self.max_message_with_image:
                raise ValidationError(
                        'Message with picture cannot exceed %s symbols!' % \
                            self.max_message_with_image)
        elif len(self.cleaned_data['message']) > self.max_single_message:
            raise ValidationError('Plain message cannot exceed %s symbols!' % \
                                    self.max_single_message)
        return self.cleaned_data['message']

    class Meta:
        model = Post
