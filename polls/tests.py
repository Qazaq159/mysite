from unittest.mock import patch

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from polls.models import Question, Choice, Publication, Article



class PollsApiTests(APITestCase):
    def test_index_view(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("You're at the polls index.", response.content.decode())

    @patch('polls.views.time.sleep', return_value=None)
    def test_run_thread_view(self, _mock_sleep):
        url = reverse('polls:run-thread') if self._has_namespace() else '/polls/run_thread'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"body": "Task successfully started!"})

    def _has_namespace(self):
        # Helper for environments where polls urls included with namespace; fall back to hardcoded path
        try:
            reverse('polls:run-thread')
            return True
        except Exception:
            return False

    # ---- Question endpoints ----
    def test_question_crud(self):
        list_url = reverse('question-list')

        # List (empty)
        response = self.client.get(list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

        # Create
        create_payload = {
            'opened': True,
        }
        response = self.client.post(list_url, data=create_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        q_id = response.data['id']
        self.assertTrue(Question.objects.filter(id=q_id).exists())

        # Retrieve
        detail_url = reverse('question-detail', args=[q_id])
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], q_id)

        # Update (partial)
        response = self.client.patch(detail_url, data={'opened': False}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['opened'], False)

        # Delete
        response = self.client.delete(detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Question.objects.filter(id=q_id).exists())

    # ---- Choice endpoints ----
    def test_choice_list_create_and_detail(self):
        # Create a question for FK
        q = Question.objects.create(opened=True)

        list_url = reverse('choice-list')
        payload = {
            'question': q.id,
            'choice_text': 'Option A',
            'votes': 0,
        }
        response = self.client.post(list_url, data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        c_id = response.data['id']
        self.assertTrue(Choice.objects.filter(id=c_id).exists())

        # List should contain the created choice
        response = self.client.get(list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

        # Detail
        detail_url = reverse('choice-detail', args=[c_id])
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['choice_text'], 'Option A')

    # ---- Publication endpoints ----
    def test_publication_create_and_detail(self):
        list_url = reverse('publication-list')
        response = self.client.post(list_url, data={'title': 'Pub 1'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        p_id = response.data['id']
        self.assertTrue(Publication.objects.filter(id=p_id).exists())

        # Retrieve
        detail_url = reverse('publication-detail', args=[p_id])
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Pub 1')

    # ---- Article endpoints ----
    def test_article_create_list_and_detail(self):
        list_url = reverse('article-list')
        # Create without publications
        response = self.client.post(list_url, data={'headline': 'Art 1'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        a_id = response.data['id']
        self.assertTrue(Article.objects.filter(id=a_id).exists())

        # List
        response = self.client.get(list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

        # Detail
        detail_url = reverse('article-detail', args=[a_id])
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], a_id)

    # ---- Flight and FlightLeg list endpoints sanity ----
    def test_flight_and_flightleg_lists(self):
        response = self.client.get(reverse('flight-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(reverse('flightleg-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
