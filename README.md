---
title: "Project Consensus"
Institution: 
  | University of Chicago
author: 
  | M.A. Camacho Jonathan 
  | Dr. Valentin Danchev
---

We seek to understand how the use of p-value evolved historically. Using Sociological theories of institutionalization and collective attention, and Computational methods, we hypothesized that the institutionalization of p-values led to a decrease on the level of its specification in research articles, signifying that p-values are taken-for-granted. We expect to contribute to debates about the misuse of p-values in academic fields such as life sciences, biomedical sciences, and psychology.

We conduct a data mining by managing, cleaning, and transforming data from 300,000+ public health articles from JSTOR and Europe PMC, and mined p-values from text by querying a relational database of 1,200,000+ entries using R, Python, and SQL. 
## Files

1. GetPvaluesEuropePMC_jonathan.r

This is an script that interfaces the Europe PMC API and extracts p-values using a list of terms to search in text extracted from a dataframe. Then it saves a R.data file with the pmcids.


- Consensus.ipynb: Interface python/MySQL function for querying a distributed database.
- config.ini: database access info. It is not included in the repo. (No included in repo)
- functions.py: Helper functions for database querying interface.  
- clean_journals.R: Creates a master list from JSTOR and Europe PMC publications.
- jstor_journals_checker.ipynb: Explores JSTOR and Europe PMC publications.

