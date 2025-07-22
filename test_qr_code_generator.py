import unittest
import os
from qr_code_generator import generate_qr_code

class TestQRCodeGenerator(unittest.TestCase):

    def setUp(self):
        self.valid_data = "https://example.com"
        self.svg_file = "test_qrcode.svg"
        self.png_file = "test_qrcode.png"

    def tearDown(self):
        if os.path.exists(self.svg_file):
            os.remove(self.svg_file)
        if os.path.exists(self.png_file):
            os.remove(self.png_file)

    def test_generate_qr_code_success(self):
        result = generate_qr_code(self.valid_data, self.svg_file, self.png_file)
        self.assertTrue(result)
        self.assertTrue(os.path.exists(self.svg_file))
        self.assertTrue(os.path.exists(self.png_file))

    def test_generate_qr_code_empty_string(self):
        with self.assertRaises(ValueError):
            generate_qr_code("")

if __name__ == "__main__":
    unittest.main()
