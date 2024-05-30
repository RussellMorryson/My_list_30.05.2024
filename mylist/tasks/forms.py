from django import forms

TAGS =(
    ("1", "Обычное"),
    ("2", "Важное"),
    ("3", "Особо важное"),
    ("4", "Немедленно")
)

class AddNewTask(forms.Form):
    title = forms.CharField(max_length=255, label='Название задачи', widget=forms.TextInput(attrs={'class': 'form-input'}))
    description = forms.CharField(max_length=3000, label='Описание', widget=forms.Textarea(attrs={'cols': 60, 'rows': 7}))
    term = forms.CharField(max_length=32, label='Срок выполнения ', required=False)
    tag = forms.ChoiceField(label='Тэг', choices = TAGS, required=False)

class EditTask(forms.Form):
    title = forms.CharField(max_length=255, label='Название задачи', widget=forms.TextInput(attrs={'class': 'form-input'}))
    description = forms.CharField(max_length=3000, label='Описание', widget=forms.Textarea(attrs={'cols': 60, 'rows': 7}))
    term = forms.CharField(max_length=32, label='Срок выполнения ', required=False)
    tag = forms.ChoiceField(label='Тэг', choices = TAGS, required=False)
    status = forms.CharField(max_length=255, label='Статус', required=False)