from Extraction import Extraction
from Transformation import Transformation
from Load import Load
import os


all_names = Extraction()


top_fives = Transformation(all_names)

print(top_fives)

export = Load()

if not os.path.exists('sheetId.txt'):
    export.make_spreadsheet()     

export.load_data_to_sheet(top_fives)