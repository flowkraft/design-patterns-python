import subprocess
import os

# Base directory for your projects and tests
base_dir = 'design-patterns-python'

# List of test files
test_files = ['tests/gof_creational_abstract_factory_test.py']

for test_file in test_files:
    print(f"Running tests for {test_file}")
    subprocess.run(['pytest', os.path.join(base_dir, test_file)])