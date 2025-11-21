

def reverse_string(s: str) -> str:
    return s[::-1]


def is_palindrome(s: str) -> bool:
    s_clean = ''.join(c.lower() for c in s if c.isalnum())
    return s_clean == s_clean[::-1]
