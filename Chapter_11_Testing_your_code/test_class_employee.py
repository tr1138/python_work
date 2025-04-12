from employee import Employee
import pytest

@pytest.fixture
def employee():
    """Employee that will be available to all tests"""
    employee = Employee('John', 'Cat', 85_000)
    return employee

def test_give_default_raise(employee):
    """Tests that the default raise of 5000 is applied by the give_raise 
    method."""
    employee.give_raise()
    assert employee.annual_salary == 90_000

def test_give_custom_raise(employee):
    """Tests that a custom raise is applied correctly."""
    employee.give_raise(10_000)
    assert employee.annual_salary == 95_000