import subprocess
import os
import sys

# Base directory for your projects and tests
base_dir = os.path.dirname(os.path.abspath(__file__))

# Add the base directory to the PYTHONPATH
sys.path.insert(0, base_dir)

# List of test files
test_files = ['patterns/gof_creational_abstract_factory_test.py']

for test_file in test_files:
    print(f"Running tests for {test_file}")
    subprocess.run(['python', '-m', 'unittest', os.path.join(base_dir, test_file)])