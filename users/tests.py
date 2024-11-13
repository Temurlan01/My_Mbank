from django.test import TestCase
from users.models import CustomUser
class GetProfileTestCase(TestCase):

    def test_profile_success(self):

        CustomUser.objects.create_user(phone_number='123456789', password='1234', balance=777)  # создаем пользователя

        self.client.login(username='123456789', password='1234')  # логиним нашего пользователя: чтобы далее он мог делать запросы от имени этого пользователя

        response = self.client.get('/my-profile/')  # делаем запрос и получаем ответ

        self.assertEqual(response.status_code, 200)  # проверяем статус код

        data = response.rendered_content  # получаем html код ответа
        print(data)
        self.assertIn('777сом', data)  # проверяем есть ли в html коде баланс нашего пользователя
