from django import forms


class DocumentForm(forms.Form):
    docfile = forms.FileField(label='Select a file')
    person_name = forms.CharField(initial='Enter person name')
    list_home_members = [
        ('usr1', 'User1'),
        ('usr2', 'User2'),
        ('usr3', 'User3'),
    ]
    home_member = forms.ChoiceField(choices=list_home_members)
    comment = forms.CharField(label='Enter a comment', widget=forms.Textarea)
