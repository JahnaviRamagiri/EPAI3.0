from assignment_s7_epai import *
import pytest
import os


def stringlen_check1():
    """
    less than 50
    :return:
    """
def stringlen_check2():
    """
    doclength more than 50 charecters.
    Written for the purpose of test
    :return:
    """


def stringlen_check3():
    """
    """
    pass

def stringlen_check4():
    pass

def test_docstringlen_none():
    with pytest.raises(ValueError):
        doc_check(stringlen_check4)


def test_docstringlen_zero():
    fn1 = doc_check(stringlen_check3)
    assert fn1 == 0


def test_docstringlen_true():
    fn1 = doc_check(stringlen_check2)
    assert fn1 == True


def test_docstringlen_false():
    fn2 = doc_check(stringlen_check1)
    assert fn2 == False


def test_fib():
    fn1 = closure_fib()
    for i in range(9):
        fn1()
    result = fn1()
    assert result == 89


def test_func_counter1():
    call = closure_func_counter()
    for i in range(5):
        call(add)
        call(mul)
        call(div)
    result = call(div)
    assert result == {'add': 5, 'div': 6, 'mul': 5}

def test_func_counter1_no_add():
    call = closure_func_counter()
    for i in range(5):
        call(mul)
        call(div)
    result = call(div)
    assert result == {'div': 6, 'mul': 5}


def test_func_counter1_only_add():
    call = closure_func_counter()
    for i in range(5):
        call(add)
    result = call(add)
    assert result == {'add': 6}


def test_func_counter2():
    input_dict1 = {}
    input_dict2 = {}
    # print(input_dict1,input_dict2)
    call1 = closure_func_counter2()
    call2 = closure_func_counter2()

    for i in range(8):
        call1(add, input_dict1)
        call1(mul, input_dict1)
        call1(div, input_dict1)

    for i in range(12):
        call2(add, input_dict2)
        call2(mul, input_dict2)
        call2(div, input_dict2)

    result = call1(div, input_dict1)
    result1 = call2(div, input_dict2)
    assert result == {'add': 8, 'mul': 8, 'div': 9}
    assert result1 == {'add': 12, 'mul': 12, 'div': 13}


def test_func_counter2_no_add():
    input_dict1 = {}
    input_dict2 = {}
    # print(input_dict1,input_dict2)
    call1 = closure_func_counter2()
    call2 = closure_func_counter2()

    for i in range(3):
        call1(mul, input_dict1)
        call1(div, input_dict1)

    for i in range(5):
        call2(mul, input_dict2)
        call2(div, input_dict2)

    result = call1(div, input_dict1)
    result1 = call2(div, input_dict2)
    assert result == {'mul': 3, 'div': 4}
    assert result1 == {'mul': 5, 'div': 6}


def test_func_counter2_only_add():
    input_dict1 = {}
    input_dict2 = {}
    # print(input_dict1,input_dict2)
    call1 = closure_func_counter2()
    call2 = closure_func_counter2()

    for i in range(3):
        call1(add, input_dict1)

    for i in range(5):
        call2(add, input_dict2)

    result = call1(add, input_dict1)
    result1 = call2(add, input_dict2)
    assert result == {'add': 4}
    assert result1 == {'add': 6}


#README tests
def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r", encoding='utf-8')
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 100, "Make your README.md file interesting! Add atleast 500 words"

