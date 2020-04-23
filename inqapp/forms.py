from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser,Question



class SignUpForm(UserCreationForm):
    # email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username','college','name','mobile')
    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        print(cleaned_data)
        name = cleaned_data.get('name')
        username = cleaned_data.get('email')
        mobile = cleaned_data.get('mobile')
        college = cleaned_data.get('college')
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username','college','name','mobile')

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        #fields = ('username', 'email','college','score','name',)
        fields = UserChangeForm.Meta.fields


class ReplyForm(forms.ModelForm):
	class Meta:
		model=Question
		fields=('answer',)
