##############################################
# p-values extractor
# This script extracts the p-values from
##############################################

#### Libraries ###############################
import pandas as pd
import re

### Funtions #################################
def extract_p_values(text, label):
    # A function to extract p values from a string of text
    # [^a-zA-Z0-9*_] is any non-whitespace and non-symbol (*#†)
    # the [0]? matches zero or one '0', some p values are reported as "p < .001"
    regex = re.compile("[^a-zA-Z0-9*#†_][Pp][\s]*[=<>≤≥][\s]*[01]?[.][\d]+")
    matches = regex.findall(text)
    pvals = []
    # strip the first character, then the 'p' or 'P'
    for i, match in enumerate(matches):
        match = "".join(match.split()) # remove all whitespace

        # now extract just the 'p=' part...
        regex = re.compile("[Pp][\s]*[=<>≤≥][\s]*[01]?[.][\d]+")
        match = regex.findall(match)[0]
        operator = match[1]
        val = match[2:]
        decimal_places = len(val.split('.')[1])
        val = float(val)
        if val <= 1.0:
          pval = [operator, val, decimal_places, label]
          pvals.append(pval)

    return(pvals)

# Setting input directory.
datadir = "./data/"
input_data_path = datadir + "abstracts.csv"

abstracts = pd.read_csv(input_data_path)
abstracts.drop(['Unnamed: 0'], axis = 1, inplace=True)

#whReleases['tokenized_text'] = whReleases['text'].apply(lambda x: nltk.word_tokenize(x))

abstracts["pvalues"]  = abstracts['abstract'].apply(lambda x: extract_p_values(x, "abstract"))
print(abstracts['pvalues'].notnull)


#pvalues = extract_p_values(str(abstracts["abstract"]), "abstract")

#print(pvalues)

