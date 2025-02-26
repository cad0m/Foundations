# DEUST Data Extractor

#### Video Demo: [Watch on YouTube](https://youtu.be/S9Vcu7jHA9Q)

#### Description:
The DEUST Data Extractor is a command-line tool designed to facilitate the extraction of student data from the DEUST website of the Faculty of Science and Technology at Mohammed V University in Rabat, Morocco. This tool enables users to extract data in either CSV or SQLite database format, providing flexibility to accommodate their specific needs.

The DEUST website serves as a crucial resource for students, faculty, and staff, offering access to vital information such as course schedules, grades, and student records. Manual extraction of data from the website is often time-consuming and error-prone. The DEUST Data Extractor automates this process, streamlining data extraction and analysis.

## Project Files

### project.py
This file serves as the main script containing the `main()` function and all project-related functions. It includes:

- **Main Function**: The command-line interface simplifies usage, allowing users to run the script, input parameters, and obtain desired results effortlessly. Users are prompted with a clear project title and instructed to provide necessary arguments to generate the desired output.
  
- **`download_pdf(filiere)`**: Downloads the PDF file corresponding to the provided field of study (`filiere`).

- **`extract_massar_codes(filiere, base_massar)`**: Converts the downloaded PDF file into a CSV format and extracts the MASSAR codes of students.

- **`get_data(html_code)`**: Extracts student data from the provided HTML code.

- **`get_html_code(massar_code)`**: Searches for student data using the MASSAR code.

- **`create_database_file(filiere, file_format, number_to_extract='all', base_massar='R137458240')`**: Generates the final CSV or SQLite database file containing extracted student data.

### test_project.py
This file serves as the main testing suite for `project.py` functions, containing:

- **`test_download_pdf()`**: Tests the `download_pdf()` function, ensuring correct download of the PDF file for the specified field of study (`filiere`) and proper saving in the current working directory. It also verifies that an error is raised for invalid `filiere` parameters.

- **`test_extract_massar_codes()`**: Verifies the functionality of `extract_massar_codes()` by ensuring correct extraction of MASSAR codes from the downloaded PDF file and returning them as a list. It includes testing for error handling with invalid `filiere` parameters.

- **`test_get_html_code()`**: Tests the `get_html_code()` function, validating the extraction of HTML code for the provided MASSAR code and ensuring it matches expected output. Error handling for invalid MASSAR codes is also covered.
