# sizer-and-merger
Combining the functionality of previous 2 projects in an interactive popup. 

First is a pdf merger whereby users can choose a folder and all the pdfs within it will be appended according to the listing as listed in the file explorer. Second is a file sizer that enumerates recursively the folder chosen to list out all files in descending order of file size, to help with file management/deletion. I have a pre-made folder named 'C:\walktest' for demonstration purposes. The folder hierarchy is as follows:

![image](https://user-images.githubusercontent.com/39832806/147831109-dee9c5fa-a4f8-4c2e-95eb-e1c6b21fd100.png)

# Table of Contents
1. [Running the script](#Running the script)
2. [Pdf merger](#Pdf merger)
3. [File Sizer](#File Sizer)




# Running the script
------------------
The popup appears for the user to choose the next action: merging pdf files or getting file sizes of all files in a path

![image](https://user-images.githubusercontent.com/39832806/147831788-7bbf2aea-981d-44fa-afef-e33198c1d7fc.png)





# Pdf merger:
------------------
If the user clicks on pdf merger, the next popup will show:

![image](https://user-images.githubusercontent.com/39832806/147831248-480f1b21-e1b8-458e-b1e8-f16f30b34a97.png)

THe user can then click on browse to open a file explorer and choose a folder with contents of pdf files to merge:

![image](https://user-images.githubusercontent.com/39832806/147831507-bdb7a30f-bbd0-4930-9ab6-6259b567af92.png)

The user will then name the output pdf merged file:

![image](https://user-images.githubusercontent.com/39832806/147831515-84b53b51-4939-4625-8deb-2512b75b7f33.png)

The user will confirm the chosen folder with displayed pdf contents:

![image](https://user-images.githubusercontent.com/39832806/147831383-e7c430b0-f28b-4950-b871-48e1a1479035.png)

Upon successful merger, a popup will notify the user:

![image](https://user-images.githubusercontent.com/39832806/147831582-c49447b6-d69d-4c87-9dd8-4d385121f4af.png)







# File Sizer:
-----------------

If the user clicks on the file sizer, the another popup will appear to prompt the user on what folder to enumerate:

![image](https://user-images.githubusercontent.com/39832806/147831801-4945da81-280e-4999-8dfa-17fbbaf2917d.png)


When the user clicks on browse, the file explorer opens for the user to choose the desired folder:

![image](https://user-images.githubusercontent.com/39832806/147831852-da15a8fc-9d7a-44c7-a180-4e73829d9fcd.png)

The user then names his desired output file. The output is a text file in a report format with headers of file size in KB followed by full filepath. This report is arranged in descending order of file size, largest file being at the top. I desinged it this way so that I can easily see what files are taking up the most space and if they are up for deletion.

![image](https://user-images.githubusercontent.com/39832806/147831921-95943f4b-5268-4a3f-a88f-9da293e4e0b5.png)

Upon successful report creation, a popup will notify the user accordingly:

![image](https://user-images.githubusercontent.com/39832806/147831964-f26bea01-8ddf-4ddc-8157-0c5bcd60eaad.png)

The file output is as follows, and is correctly created. We can also see that our previously created 'merger_demo.pdf' has also been accounted for:

![image](https://user-images.githubusercontent.com/39832806/147831988-d16c12ff-ab25-47be-b640-0294d528b63f.png)


