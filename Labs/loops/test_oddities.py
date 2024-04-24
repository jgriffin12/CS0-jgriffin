"""Test cases for oddities.py"""
import oddities


def test_answer():
    """Test answer function."""
    ans = oddities.answer(10)
    expected = "10 is even"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"


def test_answer2():
    """Test answer function for negavitve odd number."""
    ans = oddities.answer(-199)
    expected = "-199 is odd"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"


# FIXED6: add a new test case  function to test your answer function
def test_answer3():
    """Test answer function for positive odd number."""
    ans = oddities.answer(5)
    expected = "5 is odd"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"


# FIXED7: add a new test case function to test your answer function
def test_answer4():
    """Test answer function for negavitve even number."""
    ans = oddities.answer(-4)
    expected = "-4 is odd"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

def test_odd_even():
    """Test odd_even function.
    """
    ans = oddities.odd_even(10)
    expected = "even"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"


def test_odd_even2():
    """Test odd_even function for negavitve odd number
    """
    ans = oddities.odd_even(-199)
    expected = "odd"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"


# FIXED8: add a new test case function to test your answer function
def test_odd_even3():
    """Test odd_even function for negavitve odd number
    """
    ans = oddities.odd_even(5)
    expected = "odd"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

# FIXED9: add a new test case function to test your answer function
def test_odd_even4():
    """Test odd_even function for negavitve odd number
    """
    ans = oddities.odd_even(-4)
    expected = "even"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"