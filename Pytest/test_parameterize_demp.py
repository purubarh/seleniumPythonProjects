
def sum(a, b):
    return a + b

def test_calculate_sum_1():
    result =  sum(10, 20)
    assert result == 30

def test_calculate_sum_2():
    result =  sum(40, 20)
    assert result == 60

def test_calculate_sum_3():
    result =  sum(5, 20)
    assert result == 25