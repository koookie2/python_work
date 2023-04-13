import pytest
from ex_11_3_employee import Employee

@pytest.fixture
def employee():
    employee = Employee('Kavin', 'Wesley', 5000)
    return employee

def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.annual_salary == 10000

def test_give_custom_raise(employee):
    employee.give_raise(10000)
    assert employee.annual_salary == 15000