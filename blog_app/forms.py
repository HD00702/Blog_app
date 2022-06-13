from django import forms
from blog_app.models import Post
class PostForm(forms.ModelForm):  #create a form for the create page

    class Meta():
        model = Post
        fields =('title', 'content')
        widgets= {'title':forms.TextInput(),'content':forms.Textarea() }
