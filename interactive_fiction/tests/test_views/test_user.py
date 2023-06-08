import pytest
from django.contrib.auth.models import User
from django.urls import reverse


@pytest.mark.django_db
def test_registration_form(client):
    url = reverse('registration')  # Замените 'registration' на имя URL-шаблона для вашей view
    data = {
        'username': 'testuser',
        'email': 'test@example.com',
        'password1': 'testpassword',
        'password2': 'testpassword',
    }
    response = client.post(url, data)

    # Проверка, что пользователь создан и успешно вошел в систему
    assert response.status_code == 302  # Проверяем, что произошло перенаправление
    assert response.url == '/'  # Проверяем, что перенаправление ведет на указанный адрес

    user = User.objects.get(username='testuser')
    assert user.check_password('testpassword')  # Проверяем, что пароль установлен правильно
    assert user.email == 'test@example.com'  # Проверяем, что email установлен правильно
    assert user.is_authenticated  # Проверяем, что пользователь вошел в систему
