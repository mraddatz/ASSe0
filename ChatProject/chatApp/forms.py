from django import forms
from django.db import transaction
from .models import Message
import datetime


class MessageForm(forms.Form):

    text = forms.CharField(
            label='text',
            max_length=300,
            min_length=1,
    )

    alias = forms.CharField(
            label='alias',
            max_length=50,
            min_length=1,
    )

    @transaction.atomic
    def save(self):
        cleaned_data = super(MessageForm, self).clean()
        cleaned_data['pub_date'] = datetime.datetime.now()
        message = Message.objects.create(**cleaned_data)
        return message