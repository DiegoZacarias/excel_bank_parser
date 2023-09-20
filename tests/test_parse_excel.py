from parse_excel_file import parse_excel
import pandas as pd
import shutil
import tempfile
import pytest

@pytest.fixture
def temp_folder():
    # Create a temporary folder for testing
    temp_dir = tempfile.mkdtemp()
    yield temp_dir  # Provide the temporary folder path to the test
    # Teardown: Clean up the temporary folder after the test
    shutil.rmtree(temp_dir)

def test_parse_excel(temp_folder):

    target_location = temp_folder
    excel_path = 'tests/data/original.xlsx'  
    parse_excel(excel_path, target_location )

    output_path = target_location+'/parsed.csv'

    expected = pd.read_csv('tests/data/expected_output.csv')
    actual = pd.read_csv(output_path)

    assert actual.equals(expected)
