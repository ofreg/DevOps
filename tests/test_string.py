from app.string import reverse_string, is_palindrome

def test_reverse_string():
    assert reverse_string("abc") == "cba"
    assert reverse_string("") == ""

def test_is_palindrome():
    assert is_palindrome("A man a plan a canal Panama") is True
    assert is_palindrome("hello") is False
