from django.test import TestCase
from django.urls import reverse
import datetime

class CurrentDateTimeViewTests(TestCase):
    def test_current_datetime_view(self):
        response = self.client.get(reverse('current_datetime'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "It is now")

        # Check if the response contains a valid datetime string
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        self.assertIn(now[:10], response.content.decode())  # Check only the date part for simplicity
