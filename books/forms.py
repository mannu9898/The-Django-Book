from django import forms as forms
from books.models import Publisher
from django.forms import ModelForm


class PublisherForm(forms.ModelForm):
	class Meta:
		model = Publisher
		fields = ('name', 'address', 'city', 'country','website')

#PublisherForm = ModelForm(Publisher)


TOPIC_CHOICES = (
('general', 'General enquiry'),
('bug', 'Bug report'),
('suggestion', 'Suggestion'),
)



class ContactForm(forms.Form):
	topic = forms.ChoiceField(choices=TOPIC_CHOICES)
	message = forms.CharField()
	sender = forms.EmailField(required=False)


def clean_message(self):
	message = self.clean_data.get('message','')
	num_words = len(message.split())
	if num_words < 4:
		raise form.ValidationError("Not Enough words!")
	return message