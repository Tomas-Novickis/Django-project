from django.forms import ModelForm
from publisher.models import Publisher


class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']
