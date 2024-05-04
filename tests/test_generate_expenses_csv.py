from generate_expenses_csv import generate_expenses_csv
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

def test_generate_expenses_csv(temp_folder):

    target_location = temp_folder
    excel_path = 'tests/data/before_import_expenses.csv'  
    generate_expenses_csv(excel_path, target_location )

    output_path = target_location+'/expenses.csv'

    expected = pd.read_csv('tests/data/spendee_expenses.csv')
    actual = pd.read_csv(output_path)

    print(actual)
    print(expected)

    assert actual.equals(expected)
    pd_testing.assert_frame_equal(actual, expected)
