import pytest


class Test05TagAPI:

    @pytest.mark.django_db(transaction=True)
    def test_01_categories_avalible_guest_users(self, client, category_1):
        response = client.get('/api/categories/')
        assert response.status_code != 404, (
            'Страница `/api/categories/` не найдена, проверьте этот адрес в '
            '*urls.py*'
        )
        assert response.status_code == 200, (
            'Проверьте, cтраница `/api/categories/` должна быть доступна всем'
        )

        response = client.get(f'/api/categories/{category_1.id}/')
        assert response.status_code == 200, (
            'Проверьте, cтраница `/api/categories/{id}/` должна быть доступна всем'
        )
        category_1_as_dict = {
            'id': category_1.id,
            'name': category_1.name,
            'color': category_1.color,
            'slug': category_1.slug
        }
        assert response.json() == category_1_as_dict, (
            'Проверьте, что при GET запросе `/api/categories/{id}/` '
            'возвращается тег со всеми необходимыми полями'
        )
        assert response.status_code != 404, (
            'Проверьте, что при GET запросе `/api/categories/{id}/` '
            'возвращается статус 200'
        )

    @pytest.mark.django_db(transaction=True)
    def test_02_categories_prohibition_post_del_patch(
        self, client, auth_client_1, auth_client_super, category_1,
    ):
        data = {
            "name": "one",
            "color": "#0cd3a2",
            "slug": "one"
        }
        response = client.post('/api/categories/', data=data)
        assert response.status_code != 201, (
            'Проверьте, почему анонимный пользователь создает категории'
        )
        assert response.status_code == 405, (
            'Проверьте, что при POST запросе `/api/categories/` возвращается '
            'статус 405'
        )
        response = auth_client_1.post('/api/categories/', data=data)
        assert response.status_code == 405, (
            'Проверьте, что при POST запросе `/api/categories/` возвращается '
            'статус 405'
        )
        response = auth_client_super.post('/api/categories/', data=data)
        assert response.status_code == 405, (
            'Проверьте, что при POST запросе `/api/categories/` возвращается '
            'статус 405'
        )
        response = auth_client_super.delete(f'/api/categories/{category_1.id}/')
        assert response.status_code == 405, (
            'Проверьте, что при DELETE запросе `/api/categories/{id}/` возвращается'
            ' статус 405'
        )
