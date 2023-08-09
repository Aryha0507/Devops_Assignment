import unittest
from unittest.mock import patch
import App

class TestHelloWorldApp(unittest.TestCase):

    @patch("builtins.print")
    def test_hello_world_output(self, mock_print):
        App.print_hello_world()
        mock_print.assert_called_with("Hello, World!")

if __name__ == "__main__":
    unittest.main()
