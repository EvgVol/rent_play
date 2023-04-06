import pytest


class Test02FollowingAPI:

    @pytest.mark.django_db(transaction=True)
    def test_01_follow_get_users(self, client, auth_client_1):
        response = client.get('/api/users/subscriptions/')
        assert response.status_code == 401, (
            'Проверьте, что при GET запросе от анонимного пользователя'
            ' страница `/api/users/subscriptions/` возвращает статус 401'
        )
        assert response.status_code != 404, (
            'Страница `/api/users/subscriptions/` не найдена, проверьте'
            'этот адрес в *urls.py*'
        )
        response = auth_client_1.get('/api/users/subscriptions/')
        assert response.status_code == 200, (
            'Проверьте, что при GET запросе от авторизованного пользователя'
            ' страница `/api/users/subscriptions/` возвращает статус 200'
        )
        assert response.status_code != 404, (
            'Страница `/api/users/subscriptions/` не найдена, проверьте'
            'этот адрес в *urls.py*'
        )

    @pytest.mark.django_db(transaction=True)
    def test_02_follow_post_guest_users(self, client, user_2):
        response = client.post(f'/api/users/{user_2.id}/subscribe/')
        assert response.status_code != 404, (
            'Страница `/api/users/subscriptions/` не найдена, проверьте'
            'этот адрес в *urls.py*'
        )
        assert response.status_code == 401, (
            'Проверьте, что при POST запросе от анонимного пользователя'
            ' страница `/api/users/{id}/subscribe/` возвращает статус 401'
        )

    @pytest.mark.django_db(transaction=True)
    def test_03_follow_rentor_to_users(self, auth_client_1, user_2, user_4):
        response = auth_client_1.post(f'/api/users/{user_2.id}/subscribe/')
        assert response.status_code == 400,(
            'Проверьте, что при POST запросе от арендодателя'
            ' страница `/api/users/{id}/subscribe/` возвращает статус 400'
        )

        response = auth_client_1.post(f'/api/users/{user_4.id}/subscribe/')
        assert response.status_code == 400,(
            'Проверьте, что при POST запросе от арендодателя'
            ' страница `/api/users/{id}/subscribe/` возвращает статус 400'
        )

    @pytest.mark.django_db(transaction=True)
    def test_04_follow_rentor_to_self(self, auth_client_1, user_1):
        response = auth_client_1.post(f'/api/users/{user_1.id}/subscribe/')
        assert response.status_code == 400,(
            'Проверьте, что арендодатель не может подписываться на себя и'
            ' страница `/api/users/{id}/subscribe/` возвращает статус 400'
        )

    @pytest.mark.django_db(transaction=True)
    def test_05_follow_users_to_users(self, auth_client_2, user_2, user_3):
        response = auth_client_2.post(f'/api/users/{user_3.id}/subscribe/')
        assert response.status_code == 400, (
            'Проверьте, что обычный пользователь не может подписываться '
            'на других обычный пользователей страница '
            '`/api/users/{id}/subscribe/` возвращает статус 400'
        )

        response = auth_client_2.post(f'/api/users/{user_2.id}/subscribe/')
        assert response.status_code == 400, (
            'Проверьте, что обычный пользователь не может подписываться '
            'на себя страница `/api/users/{id}/subscribe/` возвращает '
            'статус 400'
        )

    @pytest.mark.django_db(transaction=True)
    def test_06_follow_users_to_rentor(self, auth_client_2, user_1):
        response = auth_client_2.post(f'/api/users/{user_1.id}/subscribe/')
        assert response.status_code == 201, (
            'Проверьте, что обычный пользователь может подписываться '
            'на арендодателей страница `/api/users/{id}/subscribe/` '
            'возвращает статус 201'
        )

        response = auth_client_2.post(f'/api/users/{user_1.id}/subscribe/')
        assert response.status_code == 400, (
            'Проверьте, что при наличии подписки'
            ' страница `/api/users/{id}/subscribe/` возвращает статус 400'
        )

        response = auth_client_2.get(f'/api/users/subscriptions/')
        assert response.status_code == 200, (
            'Проверьте, что обычный пользователь может подписываться '
            'на арендодателей страница `/api/users/{id}/subscribe/` '
            'возвращает статус 200'
        )
        data = response.json()
        assert 'count' in data, (
            'Проверьте, что при GET запросе `/api/users/subscriptions/` '
            'возвращаете данные с пагинацией. Не найден параметр `count`'
        )
        assert 'next' in data, (
            'Проверьте, что при GET запросе `/api/users/subscriptions/` '
            'возвращаете данные с пагинацией. Не найден параметр `next`'
        )
        assert 'previous' in data, (
            'Проверьте, что при GET запросе `/api/users/subscriptions/` '
            'возвращаете данные с пагинацией. Не найден параметр `previous`'
        )
        assert 'results' in data, (
            'Проверьте, что при GET запросе `/api/users/subscriptions/` '
            'возвращаете данные с пагинацией. Не найден параметр `results`'
        )
        assert data['count'] == 1, (
            'Проверьте, что при GET запросе `/api/users/subscriptions/` '
            'возвращаете данные с пагинацией. Значение параметра `count` '
            'не правильное'
        )
        assert type(data['results']) == list, (
            'Проверьте, что при GET запросе `/api/users/subscriptions/` '
            'возвращаете данные пагинацией. Тип параметра `results` должен '
            'быть список'
        )
        assert type(data['results'][0].get('consoles')) == list, (
            'Проверьте, что при GET запросе `/api/users/subscriptions/` '
            'возвращаете данные пагинацией. Тип параметра `consoles` должен '
            'быть список'
        )
        assert (
            len(data['results']) == 1
            and data['results'][0].get('username') == user_1.username
            and data['results'][0].get('email') == user_1.email
        ), (
            'Проверьте, что при GET запросе `/api/users/subscriptions/` '
            'возвращаете данные с пагинацией. Значение параметра `results` '
            'не правильное'
        )
        user_1_as_dict = {
            'id': user_1.id,
            'username': user_1.username,
            'email': user_1.email,
            'first_name': user_1.first_name,
            'last_name': user_1.last_name,
            'role': user_1.role,
            'birthdate': user_1.birthdate,
            'consoles': [],
            'is_subscribed': True,
        }
        assert data['results'] == [user_1_as_dict], (
            'Проверьте, что при GET запросе `/api/users/subscriptions/` '
            'возвращается искомый пользователь со всеми необходимыми полями, '
            'включая `is_subscribed`, `consoles`'
        )
        response = auth_client_2.delete(f'/api/users/{user_1.id}/subscribe/')
        assert response.status_code == 204, (
            'Проверьте, что при DELETE запросе и при наличии подписки'
            ' страница `/api/users/{id}/subscribe/` возвращает статус 204'
        )

    # @pytest.mark.django_db(transaction=True)
    # def test_03_follow_del_guest_users(self, client, user_2):
    #     response = client.delete(f'/api/users/{user_2.id}/subscribe/')
    #     assert response.status_code != 404, (
    #         'Страница `/api/users/subscriptions/` не найдена, проверьте'
    #         'этот адрес в *urls.py*'
    #     )
    #     assert response.status_code == 401, (
    #         'Проверьте, что при DELETE запросе от анонимного пользователя'
    #         ' страница `/api/users/{id}/subscribe/` возвращает статус 401'
    #     )

    # @pytest.mark.django_db(transaction=True)
    # def test_04_follow_del_auth_users(self, auth_client_1, user_2):
    #     response = auth_client_1.delete(f'/api/users/{user_2.id}/subscribe/')
    #     assert response.status_code == 404 or 400, (
    #         'Проверьте, что при DELETE запросе от авторизованного '
    #         'пользователя страница `/api/users/{id}/subscribe/` '
    #         'возвращает статус: `Объект не найден` или `Ошибка подписки`'
    #     )
