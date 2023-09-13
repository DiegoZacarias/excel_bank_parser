import os
import pytest
from pytest import MonkeyPatch

from file_operations import create_folder

@pytest.fixture
def mock_inputs():
    inputs = ['09', '2023']
    monkeypatch = MonkeyPatch()
    monkeypatch.setattr('builtins.input', lambda x: inputs.pop(0))
    return monkeypatch

def test_create_folder(mock_inputs):
    project_dir = os.getcwd()
    folder_path = create_folder(project_dir)
    expected_path = os.path.join(project_dir, 'bank_files', '09_2023')

    assert os.path.exists(folder_path) 
    assert folder_path == expected_path
