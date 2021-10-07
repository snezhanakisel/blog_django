from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Введите почту',
                             required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Введте почту'})
    )
    username = forms.CharField(label='Введите логин',
                               required=True,
                               help_text='Нельзя вводить символы: @, #, !',
                               widget=forms.TextInput(attrs={'class':'form-control',
                                                             'placeholder': 'Введите логин'}))
    # some = forms.ModelChoiceField(queryset=User.objects.all())
    password1 = forms.CharField(label='Введите пароль',
                                required=True,
                                help_text='Пороль должен быть больше 8 символов',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пороль'}))
    password2 = forms.CharField(label='Подтвердите пороль',
                                required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пороль еще раз'}))

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label='Введите почту',
                             required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Введте почту'})
                             )
    username = forms.CharField(label='Введите логин',
                               required=True,
                               help_text='Нельзя вводить символы: @, #, !',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Введите логин'}))

    class Meta:
        model = User
        fields = ['email', 'username']


class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(label='Загрузите фото',
                             required=False,
                           widget=forms.FileInput()
                             )

    class Meta:
        model = Profile
        fields = ['img']