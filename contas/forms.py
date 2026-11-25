from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

User = get_user_model()


class EntrarForm(AuthenticationForm):
    """Login por e-mail (o e-mail é guardado também como username)."""

    error_messages = {
        "invalid_login": "E-mail ou senha incorretos.",
        "inactive": "Esta conta está inativa.",
    }

    username = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(attrs={
            "class": "input",
            "placeholder": "voce@email.com",
            "autocomplete": "email",
            "autofocus": True,
        }),
    )
    password = forms.CharField(
        label="Senha",
        strip=False,
        widget=forms.PasswordInput(attrs={
            "class": "input",
            "placeholder": "••••••••",
            "autocomplete": "current-password",
        }),
    )

    def clean_username(self):
        return self.cleaned_data["username"].strip().lower()


class CadastroForm(UserCreationForm):
    first_name = forms.CharField(
        label="Nome",
        max_length=150,
        widget=forms.TextInput(attrs={
            "class": "input",
            "placeholder": "Como podemos te chamar?",
            "autocomplete": "given-name",
            "autofocus": True,
        }),
    )
    email = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(attrs={
            "class": "input",
            "placeholder": "voce@email.com",
            "autocomplete": "email",
        }),
    )

    field_order = ["first_name", "email", "password1", "password2"]

    class Meta:
        model = User
        fields = ("first_name", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].label = "Senha"
        self.fields["password1"].help_text = "Mínimo de 8 caracteres."
        self.fields["password2"].label = "Confirmar senha"
        self.fields["password2"].help_text = ""
        for nome in ("password1", "password2"):
            self.fields[nome].widget.attrs.update({
                "class": "input",
                "placeholder": "••••••••",
            })

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if (User.objects.filter(email__iexact=email).exists()
                or User.objects.filter(username__iexact=email).exists()):
            raise forms.ValidationError("Já existe uma conta com esse e-mail.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["email"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
