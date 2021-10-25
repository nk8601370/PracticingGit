def times_ten(number):
    return number * 100
 
# A unit test function with a single test case
def test_multiply_ten_by_zero():
    assert times_ten(0) == 0, 'Expected times_ten(0) to return 0'