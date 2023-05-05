# User Navigation Guide
This document is designed to provide you with all the information you need to navigate and use the features of the website. From the homepage to the various sections and pages, you will learn how to find what you're looking for, how to interact with different elements on the page, and how to customize your experience. The page will include step-by-step instructions, visual aids, and helpful tips to make your browsing experience smooth and efficient.
## Login Option

### Role Options
There are two main roles for this web application. Clicking "Contributor" will bring you to the Contributors Panel. And the "MLE/DS" will bring you to the MLE/DE Panel.

### Contributor Login
The contributors' page is designed to allow users to submit problem data into the database for further analysis. This page provides users with a form to upload their test and training files. Upon successful upload, a message will be displayed, and the files will be added to the database. If the upload fails, an alert message will be displayed, and the user will be asked to try again.

To submit test and training files, follow the steps below:

Step 1: Navigate to the contributors' page on the website.

Step 2: Click on the 'Upload Test File' or 'Upload Training File' button, depending on the type of file you wish to submit.

Step 3: Select the file you want to upload by clicking on the 'Choose File' button. A file explorer window will appear, allowing you to browse through your local storage to locate the file.

Step 4: Once you have selected the file, click on the 'Upload' button to initiate the upload process.

Step 5: Wait for the file to finish uploading. 

Step 6: Upon successful upload, a message will be displayed, confirming that the file has been added to the database.

Step 7: If the upload fails, an alert message will be displayed, indicating the reason for the failure. You will be asked to try again.

#### Training Data and Test Data Format 
```
Test Set,Description of Test Set,Test,Test,1,10,10,1,2023-05-02,Adam Case,,
Temperature,,,,,,,,,
Test Temp Set,,,,,,,,,
Test,,,,,,,,,
F,,,,,,,,,
Test,,,,,,,,,
0,,,,,,,,,
1,,,,,,,,,
10,,,,,,,,,
1,,,,,,,,,
TEMPERATURE,,,,,,,,,
1,,,,,,,,,
2,,,,,,,,,
3,,,,,,,,,
4,,,,,,,,,
5,,,,,,,,,
6,,,,,,,,,
7,,,,,,,,,
8,,,,,,,,,
9,,,,,,,,,
10,,,,,,,,,
```

### MLE/DS Login
The MLE (Machine Learning Engineer) role is responsible for analyzing problem data and developing solutions to improve the performance of machine learning models. This role requires users to upload solution data into the database, which includes the set ID of the problem. This page provides users with a form to upload their solution data. Upon successful upload, a message will be displayed, and the solution data will be added to the database. If the upload fails, an alert message will be displayed, and the user will be asked to try again.

Step 1: Navigate to the MLE role page on the website.

Step 2: Click on the 'Upload Solution' button.

Step 3: Select the solution file you want to upload by clicking on the 'Choose File' button. A file explorer window will appear, allowing you to browse through your local storage to locate the file. -->

> Step 4: Make sure to include the set ID of the problem in the solution document. The set ID is a unique identifier for the problem, and it is necessary to associate the solution with the correct problem in the database.

Step 5: Once you have selected the file and included the set ID, click on the 'Upload' button to initiate the upload process.

Step 6: Wait for the file to finish uploading. A progress bar will indicate the progress of the upload.

Step 7: Upon successful upload, a message will be displayed, confirming that the solution data has been added to the database. If the upload fails, an alert message will be displayed, indicating the reason for the failure. You will be asked to try again.

#### Solution File Format
```
{
    "ProblemID": "1",
    "Solution": {
      "setMeta": {
        "TS Set Name": "TS Set Name",
        "Description": "Description",
        "Application Domain(s)": "Application Domain(s)",
        "Keywords": "Keywords",
        "Vector Size": "1",
        "Min Length": "10",
        "Max Length": "10",
        "Number of TS in the Set": "1",
        "Start Datetime": "2000-12-12",
        "Contributors": "Contributors",
        "Related Paper Reference(s)": "Related Paper Reference(s)",
        "Related Paper Link": "Related Paper Link\r"
      },
      "seriesMeta": {
        "TS Name": "TEMPERATURE",
        "Description": "Description",
        "Domain(s)": "Domain(s)",
        "Units": "Units",
        "Keywords": "Keywords",
        "Scalar/Vector": "1",
        "Vector Size": "1",
        "Length": "10",
        "Sampling Period": "1"
      },
      "seriesData": {
        "point0": "1",
        "point1": "2",
        "point2": "3",
        "point3": "4",
        "point4": "4",
        "point5": "6",
        "point6": "7",
        "point7": "9",
        "point8": "9",
        "point9": "10"
      }
    }
  }
```

## Problem Viewing 
The Problems page is designed to provide users with a list of all available problems in the database. This page includes a request refresh button, which allows users to retrieve the latest problem data from the database. Users can view problem data, including the problem set ID, download the problem (training data), and view solutions attached to that problem.

Step 1: Navigate to the Problems page on the website.

Step 2: Click on the 'Request Refresh' button to retrieve the latest problem data from the database. 

Step 3: Once the refresh is complete, a list of all available problems will be displayed, including the problem set ID.

Step 4: To download the problem (training data), click on the 'Download' button next to the problem you wish to download. A file explorer window will appear, allowing you to browse through your local storage to save the file.

Step 5: To view solutions attached to a particular problem, click on the view solution button. A new pop up page will be displayed, showing all solutions attached to that problem. 

Step 7: To return to the Problems page, click on the 'Exit' button in the window.







