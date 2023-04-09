import pytest

import json

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

    @pytest.mark.django_db(transaction=True)
    def test_02_create_consoles(self, auth_client_1, auth_client_super, category_1, day, three_days):
        empty_data = {}
        response = auth_client_1.post('/api/consoles/', data=empty_data)
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе `/api/consoles/` с пустыми данными '
            'возвращаетe 400'
        )

        # data = {
        #     "name": "string",
        #     "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAgMAAABieywaAAAACVBMVEUAAAD///9fX1/S0ecCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAACklEQVQImWNoAAAAggCByxOyYQAAAABJRU5ErkJggg==",
        #     "description": "string",
        #     "barcode": "15dsfsdfssdffs2-51sdf1126825-24464288",
        #     "categories": [1],
        #     "timeframe": [
        #         json.dumps(
        #             {
        #                 "id": 1,
        #                 "price": 600
        #             },
        #         ),
        #     ]
        # }
        # response = auth_client_super.post('/api/consoles/', data=data)
        # assert response.status_code == 201, (
        #     'Проверьте, что при POST запросе `/api/consoles/` с правильными '
        #     'данными возвращает 201.'
        # )