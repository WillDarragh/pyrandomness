import importlib

test_modules = ['frequency_monobit_test']

for module in test_modules:

  importlib.import_module(module)