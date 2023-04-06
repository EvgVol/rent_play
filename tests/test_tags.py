import pytest


class Test04TagAPI:

    @pytest.mark.django_db(transaction=True)
    def test_01_tags_avalible_guest_users(self, client, tag_one):
        response = client.get('/api/tags/')
        assert response.status_code != 404, (
            'Страница `/api/tags/` не найдена, проверьте этот адрес в '
            '*urls.py*'
        )
        assert response.status_code == 200, (
            'Проверьте, cтраница `/api/tags/` должна быть доступна всем'
        )

        response = client.get(f'/api/tags/{tag_one.id}/')
        assert response.status_code == 200, (
            'Проверьте, cтраница `/api/tags/{id}/` должна быть доступна всем'
        )
        tag_one_as_dict = {
            'id': tag_one.id,
            'name': tag_one.name,
            'color': tag_one.color,
            'slug': tag_one.slug
        }
        assert response.json() == tag_one_as_dict, (
            'Проверьте, что при GET запросе `/api/tags/{id}/` '
            'возвращается тег со всеми необходимыми полями'
        )
        assert response.status_code != 404, (
            'Проверьте, что при GET запросе `/api/tags/{id}/` '
            'возвращается статус 200'
        )

    @pytest.mark.django_db(transaction=True)
    def test_02_tags_prohibition_post_del_patch(
        self, client, auth_client_1, auth_client_super, tag_one,
    ):
        data = {
            "name": "one",
            "color": "#0cd3a2",
            "slug": "one"
        }
        response = client.post('/api/tags/', data=data)
        assert response.status_code != 201, (
            'Проверьте, почему анонимный пользователь создает тэги'
        )
        assert response.status_code == 405, (
            'Проверьте, что при POST запросе `/api/tags/` возвращается '
            'статус 405'
        )
        response = auth_client_1.post('/api/tags/', data=data)
        assert response.status_code == 405, (
            'Проверьте, что при POST запросе `/api/tags/` возвращается '
            'статус 405'
        )
        response = auth_client_super.post('/api/tags/', data=data)
        assert response.status_code == 405, (
            'Проверьте, что при POST запросе `/api/tags/` возвращается '
            'статус 405'
        )
        response = auth_client_super.delete(f'/api/tags/{tag_one.id}/')
        assert response.status_code == 405, (
            'Проверьте, что при DELETE запросе `/api/tags/{id}/` возвращается'
            ' статус 405'
        )
