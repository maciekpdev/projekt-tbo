import pytest
from project.customers.models import Customer

def test_valid_input():
    customer = Customer(
        name="Important book",
        city="Warszawa",
        age=69
    )

    assert customer.city == "Warszawa"
    assert customer.name == "Important book"
    assert customer.age == 69

import pickle
import os

# B301: Deserializacja pickle jest niebezpieczna (Severity: MEDIUM)
def load_data(raw_data):
    return pickle.loads(raw_data)