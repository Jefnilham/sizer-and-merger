# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 15:30:28 2021

@author: jefni
"""

import glob
import os
from PyPDF2 import PdfFileMerger 
import PySimpleGUI as sg 


sg.theme('Dark Blue 2')   
sg.set_options(font=("Consolas", 12))
layout = [[sg.Text('My one-shot window.')],      
                 [sg.InputText(key='-IN-')],      
                 [sg.Submit(), sg.Cancel()]] 

''' 
create the first popup window 
'''



# Create the Window
window = sg.Window('Choose Action', layout)

#process "events" and get the "values" of the inputs
event, values = sg.Window('Choose Action', 
                          [[sg.Text('Select what you want to do:')], 
                           #[sg.Input(), sg.FolderBrowse()], 
                           #[sg.Text('Filename of output:')],
                           [sg.Button('Pdf Merger')], [sg.Button('File Enumerator')],
                           #[sg.Input()],
                           #[sg.OK(), sg.Cancel()] 
                           ]).read(close=True)


''' 
if user clicks on pdf merger
'''

if event == 'Pdf Merger':
    #process "events" and get the "values" of the inputs
    # Create the Window
    window = sg.Window('Pdf Merger')
    event, values = sg.Window('PDF MERGER', 
                              [[sg.Text('Select folder to merge all pdf files within:')], 
                               [sg.Input(), sg.FolderBrowse()], 
                               [sg.Text('Filename of the merged pdf file:')],
                               [sg.Input()],
                               [sg.OK()]]).read(close=True)
    
    #print('You entered', values[0], values[1])
    
    # Declare global vars 
    FOLDER = values[0]
    OUTPUT_FILE_NAME = values[1]
    OUTPUT_FILEPATH = os.path.join(FOLDER, (OUTPUT_FILE_NAME + '.pdf')) 
    #print('You entered', values[0], values[1])
    
    # Get all pdf files in folder 
    pdf_files = [] 
    
    for file in os.listdir(FOLDER): 
        if file.endswith(".pdf"): 
            if OUTPUT_FILE_NAME not in file:  
                pdf_files.append(os.path.join(FOLDER, file)) 
                
             
    number_of_files = str(len(pdf_files))
    pdf_files_copy = pdf_files.copy()
    pdf_files_copy_formated = '\n'.join(pdf_files_copy)
    # Start merging files according to list order 
    # print('Merging files in the following order:') 
    sg.popup_scrolled('You have chosen to merge ' + number_of_files + ' files listed below:', pdf_files_copy_formated, title='Confirm file merger?')
    
    print(*pdf_files, sep = "\n")
    merger = PdfFileMerger(strict=False) 
    for pdf in pdf_files: 
        merger.append(pdf) 
        
        
    # Save merged file 
    merger.write(OUTPUT_FILEPATH) 
    merger.close() 
    # print('\nOutput file saved as:', OUTPUT_FILEPATH)
    
    # successful popup
    sg.Popup('Merged file saved as:', OUTPUT_FILEPATH, title='Successful!')    


''' 
if user clicks on file enumerator
'''

if event == 'File Enumerator':
    window = sg.Window('File Enumerator')
    event, values = sg.Window('File Enumerator', 
                              [[sg.Text('Select folder to enumerate all files within:')], 
                               [sg.Input(), sg.FolderBrowse()], 
                               [sg.Text('Filename of the file size list output:')],
                               [sg.Input()],
                               [sg.OK()]]).read(close=True)

    dir_name = values[0]
    
    # recursive search with given directory name
    list_of_files = filter(os.path.isfile, glob.glob(dir_name + '/**/*', recursive=True))
    
    # enumerate to add filesize, filepath
    files_with_size = [(os.stat(files).st_size / 1000, files.replace("\\", "/", 1)) for files in list_of_files]
    
    # sort largest file at top
    files_with_size.sort(reverse=True)
    
    # write output
    with open(values[1] + '.txt', 'w') as fp:
        fp.write('Size / KB    |    Filepath\n-----------------------------------------\n')
        fp.write('\n'.join('%s    |    %s' % x for x in files_with_size))
    
    # successful popup
    sg.Popup('Enumeration report with sizes (in bytes) of all data within folder:', values[1] + '.txt', title='Successful!') 