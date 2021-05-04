## PDF CATALOGUE
A small program to create catalogues out of PDF files stored in 
a file system

### Design


#### Basic use cases:
1. Search all pdf files under a folder
2. Search a certain word in a pdf title, show list of filenames and paths
3. Search a combination of words in a pdf title, show list of filenames and paths
4. Show a list of all files found

### Use case analysis

* Use case 1: Search all pdf files under a folder
    1. Open folder and start searching for PDF files
    2. Create list with filenames and paths
    3. Store list internally
  
* Use case 2: Search a certain word in PDF titles, show list of filenames and paths to user
  1. Get word that user wants to check
  2. Search all filenames from stored list for the word
  3. For each filename that matches print the name and the path
  
* Use case 3: Search a combination of words in PDF titles, show list of filenames and paths
  1. Get words that user wants to check
  2. Search all filenames that contain all words
  3. For each filename that matches print the name and the path
  
* Use case 4: Show a list of all files found
  1. For each entry in the stored list, print filename and path 
  

  

