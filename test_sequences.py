import sequences

def test_fibonacci():
    result=sequences.fibonacci(5)
    correct=[1,1,2,3,5]
    assert result==correct
    
def test_fibonacci():
    result=sequences.fibonacci(12)
    correct=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    assert result==correct
    
def test_fibonacci3():
    result=sequences.fibonacci(17)
    correct=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
    assert result==correct