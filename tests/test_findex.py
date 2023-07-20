import hashlib
import importlib

import pytest

from infinite_fn.python_fns.trip import distance_between_two_locations


class FunctionIndexer:
    def __init__(self, function_dict=None):
        if function_dict is None:
            self.function_dict = {}
        else:
            self.function_dict = function_dict

    def index_function(self, function):
        module_name = function.__module__
        function_name = function.__qualname__  # use __qualname__ for nested functions
        identifier = f"{module_name}.{function_name}"
        if "<locals>" in identifier:
            raise ValueError("Cannot index local functions.")
        print(f"Identifier: {identifier}")
        function_hash = hashlib.sha1(identifier.encode()).hexdigest()
        self.function_dict[function_hash] = identifier
        return function_hash

    def get_function(self, function_hash):
        if function_hash not in self.function_dict:
            raise ValueError(f"No function found with hash: {function_hash}")
        identifier = self.function_dict[function_hash]
        parts = identifier.split('.')
        _fn = parts[-1]
        _mod = ""
        _last_mod = ""
        for pt in parts[:-1]:
            try:
                _last_mod = str(_mod)
                _mod += pt
                module = importlib.import_module(_mod)
                _mod += "."
                # module = importlib.import_module('.'.join(parts[:-1]))
                # function = getattr(module, _fn)
            except ModuleNotFoundError:
                print("Last module: ", _last_mod)
                module = importlib.import_module(_last_mod[:-1] if _last_mod.endswith(".") else _last_mod)
                module = getattr(module, pt)
                # print(f"Module: {getattr(module, pt)}")
        # module = importlib.import_module('.'.join(parts[:-1]))
        function = module
        part = parts[-1]
        function = getattr(function, part)
        return function


def this_is_a_test_function():
    return "Hello, World!"


class TestClass:
    def test_class_method(self):
        return "Hello, World!"


def test_function_indexer():
    # Define a function for testing

    # Instantiate FunctionIndexer
    indexer = FunctionIndexer()

    # Index the test function
    function_hash = indexer.index_function(this_is_a_test_function)

    # Get the function back using its hash
    retrieved_function = indexer.get_function(function_hash)

    # Call the retrieved function and check that it returns the expected value
    assert retrieved_function() == "Hello, World!"

    # Check that trying to get a function with a non-existent hash raises a ValueError
    with pytest.raises(ValueError):
        indexer.get_function("nonexistenthash")


def test_function_indexer_from_class():
    # Instantiate FunctionIndexer
    indexer = FunctionIndexer()

    # Index the test function
    function_hash = indexer.index_function(TestClass.test_class_method)

    # Get the function back using its hash
    retrieved_function = indexer.get_function(function_hash)

    # Call the retrieved function and check that it returns the expected value
    assert retrieved_function(TestClass()) == "Hello, World!"


def test_function_indexer_nested():
    def my_dummy_function():
        return "Hello, World!"

    # Instantiate FunctionIndexer
    indexer = FunctionIndexer()
    with pytest.raises(ValueError):
        indexer.index_function(my_dummy_function)
        function_hash = indexer.index_function(my_dummy_function)
