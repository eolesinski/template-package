from example_project_python import hello, print_hello
from unittest.mock import patch

# create a test function that tests the hello function
def test_hello():
    assert hello() == "Hello, world!"

# mock out the hello funtion to tests that the print hellp function works
@patch('builtins.print')
def test_print_hello(mock_print):
    print_hello()
    assert mock_print.call_args.args == ("Hello, world!",)
