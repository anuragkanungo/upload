# -*- coding: utf-8 -*-
from django import forms

class DocumentForm(forms.Form):
    name = forms.CharField(label = 'Enter name', required=True)
    docfile = forms.FileField(
        label='Select a file'
    )
