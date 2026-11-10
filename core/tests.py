from django.test import TestCase

from core.views import VERIFICATION_FLAG, VERIFICATION_TEXT


class HealthCheckTests(TestCase):
	def test_health_ok(self):
		response = self.client.get("/health/")

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.json()["status"], "ok")


class VerificationPageTests(TestCase):
	def test_verification_flag_is_false(self):
		self.assertFalse(
			VERIFICATION_FLAG,
			"VERIFICATION_FLAG debe permanecer en False para que la verificación pase.",
		)

	def test_verification_page_shows_configured_text(self):
		response = self.client.get("/")

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, VERIFICATION_TEXT)
