from app import greeting, add, sub, mult

def test_greet():
    assert greeting("Bob") == "Hola Bob!"

def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(20, 10) == 10

def test_mult():
    assert mult(5, 3) == 15