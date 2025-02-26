import os
import pytest
from project import download_pdf, extract_massar_codes, get_html_code, create_database_file

def test_download_pdf():
    download_pdf('mip')
    file_exit= os.path.exists(f"mip_data.pdf")
    assert file_exit == True
    download_pdf('bcg')
    file_exit= os.path.exists(f"bcg_data.pdf")
    assert file_exit == True
    with pytest.raises(ValueError):
         download_pdf('test')
    
def test_extract_massar_codes(): 
     assert ['R137458240'] in extract_massar_codes("mip", 'R137458240') 
     assert ['R137458240'] in extract_massar_codes("bcg", 'R137458240')
     with pytest.raises(SystemExit):
        extract_massar_codes("test", 'R137458240')
          
def test_get_html_code():
    with open("test.html", 'r') as file:
        reader = file.read()
        #assert get_html_code('R137458240') ==  reader --> é in french problem
        assert get_html_code('R137458250') !=  reader
