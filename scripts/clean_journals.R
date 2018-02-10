library(tidyverse)
library(readxl)
library(lubridate)
library(stringi)

jstore = read_xls("./data/journals.xls")

jstore_cleaned <- jstore %>% 
       select(title = publication_title, discipline, full_coverage, title_id, coverage_depth, publisher = publisher_name, publication_type) %>%
       separate(full_coverage, into = c("ini_date", "last_date"), sep = " - ") %>% 
       mutate(ini_year = year(ini_date), last_year = year(last_date), source = "jstor") %>% 
       filter(ini_date <= 1940 & last_date >= 2000) %>%
       select(title, discipline, ini_year, last_year, title_id, publisher, publication_type, source)

years <- as.character(1500:2017)
years_match <- str_c(years, collapse = "|")

pmc_eur = read.csv("./data/jlist.csv") 
pmc_eur_cleaned <- pmc_eur %>% 
       mutate(ini_year = year(make_date(str_extract(pmc_eur$Earliest.volume, years_match))),
              last_year = year(make_date(str_extract(pmc_eur$Latest.issue, years_match)))) %>% 
       select(title = Journal.title, discipline = NLM.TA, ini_year, last_year, Publisher) %>%
       filter(ini_year <= 1940 & last_year >= 2000) %>% 
       mutate(title_id = "na", publication_type = "na", source = "pmc europe") %>%
       select(title, discipline, ini_year, last_year, title_id, publisher = Publisher, publication_type, source)

usable_journals <- bind_rows(jstore_cleaned, pmc_eur_cleaned) %>%
       write_csv("./data/usable_journals.csv")



   