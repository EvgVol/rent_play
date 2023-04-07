import pytest


class Test05ConsolesAPI:

    @pytest.mark.django_db(transaction=True)
    def test_01_availability_consoles(self, client, auth_client_1):
        response = client.get('/api/consoles/')
        assert response.status_code == 401, (
            'Проверьте, что при GET запросе от анонимного пользователя'
            ' страница `/api/consoles/` возвращает статус 401'
        )

        response = auth_client_1.get('/api/consoles/')
        assert response.status_code == 200, (
            'Проверьте, что при GET запросе от авторизованного пользователя'
            ' страница `/api/consoles/` возвращает статус 200'
        )

    
