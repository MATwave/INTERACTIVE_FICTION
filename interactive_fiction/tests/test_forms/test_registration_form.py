import pytest
from django.urls import reverse
from ifbook.forms.registration import RegistrationForm


@pytest.mark.django_db
def test_registration_form_valid():
    form_data = {
        'username': 'testuser',
        'email': 'test@example.com',
        'password1': 'very@difficult@pass123',
        'password2': 'very@difficult@pass123',
    }

    form = RegistrationForm(data=form_data)
    assert form.is_bound
    assert form.is_valid()


@pytest.mark.django_db
def test_registration_form_invalid():
    form_data = {
        'username': 'testuser',
        'email': 'invalid_email',
        'password1': 'password123',
        'password2': 'password456',
    }

    form = RegistrationForm(data=form_data)
    assert not form.is_valid()


@pytest.mark.django_db
def test_registration_view(client):
    url = reverse('registration')

    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.context['form'], RegistrationForm)
