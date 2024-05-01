from clean_csv import actualizar_csv
import pandas as pd
import pandas.testing as pd_testing
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

def test_clean_csv(temp_folder):

    target_location = temp_folder
    excel_path = 'tests/data/parsed.csv'  
    actualizar_csv(excel_path, target_location)

    output_path = target_location+'/before_import.csv'

    expected = pd.read_csv('tests/data/before_import.csv')
    actual = pd.read_csv(output_path)

    print(expected)
    print(actual)

    assert actual.equals(expected)
    pd_testing.assert_frame_equal(actual, expected)
