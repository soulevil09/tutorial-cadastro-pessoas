from django import forms
from .models import Pessoa


class PessoaForm(forms.ModelForm):
    data_nascimento = forms.DateField(
        widget=forms.TextInput(
            attrs={"type": "date"}
        )
    )

    class Meta:
        model = Pessoa
#        fields = ('__all__')  # outra maneira de importar todos os campos para fazer o formulário
        fields = ['nome_completo', 'data_nascimento', 'ativa']
