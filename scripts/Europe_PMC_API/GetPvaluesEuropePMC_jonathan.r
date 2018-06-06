#### Script for Extracting P-values from Europe PMC ##########################
# 
# This is an script that interfaces the Europe PMC API and extracts p-values 
# using a list of terms to search in text extracted from a dataframe. Then it 
# saves a R.data file with the pmcids.
#
##############################################################################

# Libraries
library(europepmc)
library(tidyverse)


# Sets up the parameters for the function epmc_search.
body(epmc_search)[[11]] <- substitute(if (hits == 0) hits = 1)

# Checks the parameters were set-up correctly,
# print(body(epmc_search))

# Sets up term to search in text in database.
pvalue_search = read_table("./scripts/Europe_PMC_API/pvalue_search_csv.csv")
methods <- as.character(pvalue_search$V1)

# Initializes list. 
datalist = list()

# Extracts data according to parameters. 
for(i in methods[1:4]){ 
  method = sprintf("METHODS:%%22%s%%22",i)   # idetifies methos section in articles. 
  restpmc = europepmc::epmc_search(method, output = "id_list", limit = 5000)
  datalist[[i]] <- restpmc$pmcid             # Creates a pmcid list with p-values in methods section. 
  print(method)
}

print(datalist)
# Saves list of pmcids in a R.data file. 
save(datalist, file = "pvalue_search.RData")