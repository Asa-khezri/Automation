# Home Assignment
## Table of content

- Data Extraction
- Data Transformation
- Data loading
- Scheduling
- Form Generation and Data summary

---

### **Data Exteraction**

In this part names of artists from the [website Billboard]( https://www.billboard.com/charts/artist-100/) will be extracted for 4 weeks from now. Totally, we will have 400 names.
For this purpose I created a file named “**Extraction.py**”. In this file a function exist to extract all 400 artist’s names from the website and return them as two dimensional array labeled “**all_names**”
- The function name is Extraction.
- I use BeautifulSoup to extract data.

---

### **Data Transformation**
For data transformation we have 3 requirements:

- Combine the names of the top 5 artists from each of the Artist 100 lists of the past 4 weeks into one list.
- Make sure that every artist is present in the combined list once.
- The artists should be sorted alphabetically.

To implement these requirements, there is a file named “**Transformation.py**” having a function with the same name. This function gets all artist’s names and return a *sorted* *non-repetitive* names from the first 5 artists in every week. 

---


### **Data loading**

1. Create a google cloud project in the [console.cloud.google.com](https://console.cloud.google.com/projectcreate) My project is **Billboard**.
2. Enable the API: Enable the **Google Sheets API** From  **API & Services/Library**.
3. [Authorize credentials](https://developers.google.com/sheets/api/quickstart/python) for a desktop application:
   1. In the Google Cloud console, go to Menu menu > APIs & Services > Credentials.
   2. Click Create Credentials > OAuth client ID
   3. Click Application type > Desktop app.
   4. In the Name field, type a name for the credential.
   5. Click Create.
   6. Click OK. The newly created credential appears under OAuth 2.0 Client IDs.
   7. Save the downloaded JSON file, and move the file to your working directory. My json file is credentials.json

4. Install the Google client library by executing this command in the command line:

   > pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

5. Run this command to configure the sample using the file **Google.py** in the working directory: 
   - python3 Google.py
6. Give the neccessary permission

**_To create a google sheet and load our data in it, I have done as follows_**:
I created a file named **Load.py** contains a class with two methods.

- First method is "make_spreadsheet": Using the service built in the body of the class, this method creates a Google Sheet. The created sheet has a lable **Project Billboard** and work sheet with the name of **Top Fives**. This method also save the sheet ID in a text file named **sheetId.txt** for the next step.

- Second method is "load_data_to_sheet": gets name as an input and gets sheet ID bz opening the _sheetId.txt_ and load data to the created sheet in the previous step.


**_And finally by running the "ETL.py" all steps of extraction, transformation and load will be executed_**

---

### _Scheduling_

Schedule the above operations to occur once every month.
We must schedule ETL.py in order to meet this criterion.
This software, which frequently runs on a Linux server, is scheduled using the Crontab tool. 

- We can do this by running the following:
  > 0 0 1 \* \* python3 the address of python code/ETL.py
  >
  > crontab -e

---

### _Form Generation and Data summary_

In this part we have to accomplish two steps:

- Make a Google Apps script that creates a Google Form with a list of all the artists from the uploaded Google Sheet and a one-to-five rating system for each of them. 

- Make a Google Apps script that analyzes the form responses to determine the average rating of each artist and adds the average ratings next to each artist's name in the uploaded Google Sheet. 

In order to do the above we need to:

1. Copy the codes from the file "_AppScript.gs.js_" and past to the created sheet(Project Billboard) in the following address:
>  Extentions/Apps script

2. After doing the previous part, it is needed to run the script and give the neccesary premissions.
   - The triggers are written in such a way that the average is computed and added to the excel sheet with each submission of the form.
   - Codes are written so that voting for each artist is **not required**.
