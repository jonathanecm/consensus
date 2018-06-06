#### Cleans jstor and PMC raw datasets and creates a master dataset ##########
# 
# This script takes to datasets containing a full list of articles in jstor and 
# PMC Europe and cleans features and merges the datasets into one master dataset.
#
##############################################################################

# Libraries.
library(tidyverse)
library(readxl)
library(lubridate)
library(stringi)

# Reads raw dataset. 
jstore = read_xls("./data/journals.xls")

# Cleans variables in jstor dataset. 
jstore_cleaned <- jstore %>% 
       select(title = publication_title, discipline, full_coverage, title_id, coverage_depth, publisher = publisher_name, publication_type) %>%
       separate(full_coverage, into = c("ini_date", "last_date"), sep = " - ") %>% 
       mutate(ini_year = year(ini_date), last_year = year(last_date), source = "jstor") %>% 
       filter(ini_date <= 1940 & last_date >= 2000) %>%
       select(title, discipline, ini_year, last_year, title_id, publisher, publication_type, source)

# Selects years range. 
years <- as.character(1500:2017)
years_match <- str_c(years, collapse = "|")

# Cleans variables in pmc dataset. 
pmc_eur = read.csv("./data/jlist.csv") 
pmc_eur_cleaned <- pmc_eur %>% 
       mutate(ini_year = year(make_date(str_extract(pmc_eur$Earliest.volume, years_match))),
              last_year = year(make_date(str_extract(pmc_eur$Latest.issue, years_match)))) %>% 
       select(title = Journal.title, discipline = NLM.TA, ini_year, last_year, Publisher) %>%
       filter(ini_year <= 1940 & last_year >= 2000) %>% 
       mutate(title_id = "na", publication_type = "na", source = "pmc europe") %>%
       select(title, discipline, ini_year, last_year, title_id, publisher = Publisher, publication_type, source)

# Merges datasets and save them into a master set. 
usable_journals <- bind_rows(jstore_cleaned, pmc_eur_cleaned) %>%
       write_csv("./data/usable_journals.csv")



   