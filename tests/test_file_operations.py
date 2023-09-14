import os
import pytest
from pytest import MonkeyPatch
import shutil
import tempfile

from file_operations import create_folder

@pytest.fixture
def mock_inputs():
    inputs = ['09', '2023']
    monkeypatch = MonkeyPatch()
    monkeypatch.setattr('builtins.input', lambda x: inputs.pop(0))
    return monkeypatch

@pytest.fixture
def temp_folder():
    # Create a temporary folder for testing
    temp_dir = tempfile.mkdtemp()
    yield temp_dir  # Provide the temporary folder path to the test
    # Teardown: Clean up the temporary folder after the test
    shutil.rmtree(temp_dir)

# def test_create_folder(mock_inputs, temp_folder):
def test_create_folder(temp_folder):
    project_dir = temp_folder
    folder_path = create_folder(project_dir, "09", "2023")
    expected_path = os.path.join(project_dir, 'bank_files', '09_2023')

    assert os.path.exists(folder_path) 
    assert folder_path == expected_path
