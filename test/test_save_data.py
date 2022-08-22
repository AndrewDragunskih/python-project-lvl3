from page_loader.save_data import save_data
import tempfile
import os
import pytest

def test_save_data():
    data_to_save = 'test data'
    with tempfile.TemporaryDirectory() as tmp_dir_name:
        tmp_file_name = os.path.join(tmp_dir_name,'testfile.txt')
        save_data(tmp_file_name, data_to_save)
        assert os.path.isfile(tmp_file_name) is True
        with open(tmp_file_name, 'r') as created_file:
            saved_data = created_file.read()
        assert data_to_save == saved_data
    assert os.path.isfile(tmp_file_name) is False
    assert os.path.isdir(tmp_dir_name) is False
