import re
import os
import csv
import sys
import tabula
import pandas as pd
import sqlite3
import requests
from bs4 import BeautifulSoup
import pyfiglet as pyg
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



URLS = ["https://e-resultat.fstm.ac.ma/deust/deust.php", "https://e-resultat.fstm.ac.ma/deust/semestres.php"]

#pdf url can be changed every semestre first: mip, seconf: bcg
PDF_URLS = [
    'https://www.fstm.ac.ma/affaires_pedagogiques/files/2023-2024/SA/Fichier_global_reinscription_MIP_printemps_2024_.pdf',
    'https://www.fstm.ac.ma/affaires_pedagogiques/files/2023-2024/SA/Fichier_global_reinscription_BCG_printemps_2024_.pdf'
]
#path where selenium drive exist
PATH = r"C:\Program Files (x86)\chromedriver.exe"

# Downloads the PDF
def download_pdf(filiere):
    # Downloads the PDF file for the given filiere.
    if filiere == "mip":
        num = 0
    elif filiere == "bcg":
        num = 1
    else:
        raise ValueError("out of urls")
    response = requests.get(PDF_URLS[num])
    if response.status_code == 200:
        with open(f"{filiere}_data.pdf", 'wb') as f:
            f.write(response.content)
            print("PDF downloaded successfully!")
    else:
        print("PDF not downloaded")

def extract_massar_codes(filiere, base_massar):
    try:
        #initialize the list with the given massar code to create correct heaeder
        massar_codes = [[f"{base_massar}"]]
        
        #convert pdf file to csv
        tabula.convert_into(f"{filiere}_data.pdf", f"{filiere}.csv", output_format="csv", pages= 'all')
        
        #extract only massar_code from csv file
        with open(f"{filiere}.csv", "r") as file:  
            reader = csv.DictReader(file)
            for row in reader:
                codes_in_maybe = row['Nom'] + row["MASSAR"]
                code = re.findall(r"\w\d{9}", codes_in_maybe)
                if code != [f"{base_massar}"]:
                    massar_codes.append(code)
        return massar_codes
    
    except FileNotFoundError:
        sys.exit("file not found")

def get_data(html_code):
    try:
        soup = BeautifulSoup(html_code, 'lxml')
        
        #find the notes table
        table = soup.find_all("tr")
        
        #extract info from the first and second table resp
        header = [th.text.strip() for th in table[0].find_all('th')]
        student = [th.text.strip() for th in table[1].find_all('th')]
        
        #merge the header and infos in dict and return it
        return dict(zip(header, student))
    except TypeError:
        pass

def get_html_code(massar_code):
    #prepare the drive
    webdriver.chrome.driver = PATH
    driver = webdriver.Chrome()

    for i in range(2):
        #try the massar code with the first url if it doesnt work try it with the second
        driver.get(URLS[i])
        
        search = driver.find_element(By.ID,"code")
        search.send_keys(f"{massar_code}")
        search.send_keys(Keys.RETURN)
        
        #wait the page until the table load
        try:
            table = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "table.table.table-striped.table-bordered.table-condensed"))
            )
            html_code = driver.page_source
            driver.quit()
            
            #return the page with table's html code
            return html_code
        except:
            print("Invalid massar code. Trying next URL...")
    driver.quit()
    return None

def create_database_file(filiere, file_format,  number_to_extract = 'all', base_massar = 'R137458240'):
    students = []
    
    #get the list of massar_codes and
    massar_codes = extract_massar_codes(filiere, base_massar)
    
    #if the user doent give the a number to extract intialize it with the lenth of the list
    if number_to_extract == 'all':
        number_to_extract = len(massar_codes)
    
    #get the data and store it as a dict in students list
    for code in massar_codes[0:number_to_extract]:
        students.append(get_data(get_html_code(f"{' '.join(code)}")))
    
    #get the keys from from the list as a header to the csv file
    header = list(students[0].keys())
    
    #booling variable to check if the csv file is exist
    file_exit = os.path.exists(f"{filiere}_data.csv")
    
    #creat the cvs file and file it with infos
    with open(f"{filiere}_data.csv", "a", newline= "") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames= header)
        
        if not file_exit :
            writer.writeheader()
        try:
            #variable to count the numbers of fails     
            failed = 0
            for student in students:
                writer.writerow(student)
        except ValueError:
            #count and show the totale numbers of fails 
            failed += 1
            print(f"cant add this student Number of failures {failed}")
    
    #if user choose the output format as db create a database and remove the csv file
    if file_format == "db": 
        con = sqlite3.connect(f"{filiere}.db")
        df = pd.read_csv(f"{filiere}_data.csv", encoding='latin-1')
        df.to_sql("main", con, if_exists = "append")
        con.close()
        os.remove(f"{filiere}_data.csv")
    
    #clear working with files and keep only csv or bd 
    os.remove(f"{filiere}.csv")
    os.remove(f"{filiere}_data.pdf")

def main():
    
    #user interface
    print(pyg.figlet_format("           DEUST Data Extractor", font = "slant"))

    try:
        #ask user for the filiere and validate the input
        while True:
            filiere = input("choose between 'mip' or 'bcg': ")
            if filiere == 'mip' or filiere == 'bcg':
                break
        
        #ask user for the format and validate the input
        while True:
            file_format = input("choose the format between 'csv' or 'db': ")
            if file_format == 'csv' or file_format == 'db':
                break
        
        #ask user for the size of students notes and validate the input
        while True:
            data_number = int(input("choose the number of student: "))
            if data_number >= 1 :
                break
    except ValueError:
        sys.exit("invalid infos")
    
    #downlaod pdf
    download_pdf(filiere)
    
    #create the data file
    create_database_file(filiere, file_format, data_number)
    
    #print the final msg for the user
    print(f"your {file_format} file is ready :)")


if __name__ == "__main__":
    main()