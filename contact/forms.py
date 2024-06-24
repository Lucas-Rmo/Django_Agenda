from django.core.exceptions import ValidationError
from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm

class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget = forms.FileInput(
            attrs={
                "accept":"image/*",
            }
        )
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"placeholder",
                
            }
        ), 
        help_text = "texto de ajuda"
    )


    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        #pode alterar o widget desse jeito:
        #self.fields["last_name"].widget.attrs.update({
            #"placeholder":"Ultimo nome"
        #})

    class Meta:
        model = models.Contact
        fields = ("first_name","last_name","phone","email",
                  "description","category","picture",)

        # ou alterar o widget desse jeito:
       # widgets = {
            #"first_name": forms.TextInput(
            #    attrs={"class" : "classe-a classe-b",
           #            "placeholder":"Escreva aqui"}
          #  )
       # }

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")

        if first_name == last_name:
            self.add_error("first_name",
                       ValidationError(
                           "Primeir nome não pode ser igual ao segundo",
                           code="invalid"
                       ))
        return super().clean()
    
    #Validação dos campos
    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")

        if first_name =="ABC":
            self.add_error("first_name",
                        ValidationError(
                            "mensagem de erro 2",
                            code="invalid"
                        ))
        return first_name
    

class RegisterForm(UserCreationForm):
    ...