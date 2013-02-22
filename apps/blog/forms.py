from django.forms import ModelForm
from apps.blog.models import Post

class FormEntry(ModelForm):
	class Meta:
		model = Post
