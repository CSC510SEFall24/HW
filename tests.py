import pytest # type: ignore
from fibonacci import fibonacci

def test_fibonacci_positive():
    # This test will pass when we test it for any postive value of n
    fibonacci(5)

def test_fibonacci_negative():
    # This test fails due to the intentional error we added to the code which is the code will not run for all negative values of n
        fibonacci(-5)  
if __name__ == "__main__":
    pytest.main()