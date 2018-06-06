---
title: "Project Consensus"
Institution: 
  | University of Chicago
author: 
  | M.A. Camacho Jonathan 
  | Dr. Valentin Danchev
---

We seek to understand how the use of p-value evolved historically. Using Sociological theories of institutionalization and collective attention, and Computational methods, we hypothesized that the institutionalization of p-values led to a decrease on the level of its specification in research articles, signifying that p-values are taken-for-granted. We expect to contribute to debates about the misuse of p-values in academic fields such as life sciences, biomedical sciences, and psychology.

We conduct a data mining by managing, cleaning, and transforming data from 300,000+ public health articles from JSTOR and Europe PMC, and mined p-values from the text by querying a relational database of 1,200,000+ entries using R, Python, and SQL. 
## Files

1. database.connection.ipynb: 
Develops a function in python and MySQL that queries a relational database of 1,200,000+ entries at the Knowledge Lab - University of Chicago. The function establishes the connection to the database using helper functions located in the function.py file, and uses SQL DML language to select features or variables from multiple tables, performs a table merge, and creates a dataset in CSV format for further analysis. 

2. functions.py: Helper functions for database querying interface.  
File containing a series of helper functions coded in Python to aid in the analysis of p-values included in text files. 
- read_db_config: Read database configuration file and return a dictionary object.
- iter_row: Read database configuration file and return a dictionary object.
- extract_p_values: (Prototype) A function to extract p values from a string of text.

3. GetPvaluesEuropePMC_jonathan.r
This is a script in R that interfaces the Europe PMC API and extracts p-values from 170,000+ files from Europe PMC using a list of terms to search in text extracted from a dataframe. Then it saves a R.data file with the pmcids.

4. clean_journals.R
This script in R takes to datasets containing a full list of articles in jstor and PMC Europe publications and cleans features and merges the datasets into one master dataset.

5. config.ini
Database access credentials. It is not included in the repo for security reasons. 


