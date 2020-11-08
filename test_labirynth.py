import unittest
from settings import Settings
class TestLabirynth(unittest.TestCase):
	def test_h_passes_parameters_pair(self):
		settings=Settings()
		self.assertEqual(len(settings.h_pass_x),len(settings.h_pass_y))
	def test_v_passes_parameters_pair(self):
		settings=Settings()
		self.assertEqual(len(settings.v_pass_x),len(settings.v_pass_y))
unittest.main()
