from django import forms
from django.contrib.auth.models import User


class CodeForm1(forms.Form):
    code = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': '#Пиши свой код здесь', 'aria-label': 'code', 'aria-describedby': 'input-group-left', 'cols': 60, 'rows': 8, 'style': 'resize: none;'}))


class CodeForm2(forms.Form):
    code1 = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': '#Пиши свой код здесь', 'aria-label': 'code', 'aria-describedby': 'input-group-left', 'cols': 60, 'rows': 5, 'style': 'resize: none;'}))
    code2 = forms.CharField(label="", widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': '#Пиши свой код здесь', 'aria-label': 'code',
               'aria-describedby': 'input-group-left', 'cols': 60, 'rows': 5, 'style': 'resize: none;'}))


class ChoiceForm(forms.Form):
    selected_image = forms.IntegerField(widget=forms.RadioSelect())


class EmailForm(forms.Form):
    email = forms.EmailField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Пиши свою почту здесь', 'cols': 40}))


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label='Имя персонажа', widget=forms.TextInput())
    first_name = forms.CharField(label='Номер персонажа', widget=forms.TextInput())
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(), required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user
