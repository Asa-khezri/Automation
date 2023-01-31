from Google import Create_Service 


class Load:
    clientSecretFile = 'credentials.json'
    apiName = 'sheets'
    apiVersion = 'v4'
    scops = ["https://www.googleapis.com/auth/spreadsheets"]
    service = Create_Service(clientSecretFile, apiName, apiVersion, scops) 
  
    
    def make_spreadsheet(self): 
        sheet_body = {
            'properties': { 'title' : 'Project Billboard'},
            'sheets':
            [{'properties': {'title':'Top Fives' }}]
            }

        creat_sheet = self.service.spreadsheets().create(body = sheet_body).execute()
        
        #self.worksheet_name =  creat_sheet['sheets'][0]['properties']['title']+'!'
        
        sheet_ID = creat_sheet['spreadsheetId']
        with open('sheetId.txt', 'w') as saveId:
            saveId.write(sheet_ID)
        
        print('/n')
        print(f"Spreadsheet is created successfully: {creat_sheet['spreadsheetUrl']}")    

        

    def load_data_to_sheet(self, names):
        with open('sheetId.txt', 'r') as openfile:
            sheet_id  = openfile.read() 
        range = 'A1'
        value = {
            'majorDimension': 'ROWS',
            'values': [names]
        }
        self.service.spreadsheets().values().append(spreadsheetId=sheet_id, 
                                                range=range, 
                                                valueInputOption='USER_ENTERED', 
                                                body=value).execute()                                        
        
       