# CA Coast Sea-Level Rise Python Data Project Report

## 1. Introduction

Which coastal California counties are most at risk from sea-level rise? <br />
This is the environmental research question that this Python programming project seeks to answer.

<p>
The development strategy centers on fetching JSON data from the publicly available API 
of risks from sea-level rise courtesy of the CA Coastal Commission 
(<a href="https://www.coastal.ca.gov/open-data/api-docs/">https://www.coastal.ca.gov/open-data/api-docs/</a>)
and using core Python features to process, visualize, and analyze this data.
Additional datapoints will be extracted from PDF risk assessment files for each coastal California counties.
</p>

## 2. Requirements

_Required Imports (Also see the included requirements.txt)_

- import requests
- import numpy
- import pandas as pd
- import matplotlib
- import PyPDF2

## 3. Description of the Python programs

The development project consists of the following four main python programs:

1. **api_data_utils.py**<br />
   This user-created module handles hitting the API endpoint with the fetch_and_parse_json() function,<br />
   and is imported by other files that use this fetched data.
   <br />&nbsp;<br />

2. **ccc_risk_factors.ipynb**<br />
   This program processes and visualizes the CA Coastal Commission (CCC) Risk Factors, summing up
   risk factors from infrastructure and energy to beaches and public access recreation.
   It uses pandas and matplotlib to create a bar chart data visualization for risks by county.
   <br />&nbsp;<br />

3. **shoreline_miles_as_risk_proxy.ipynb**<br />
   This program processes and visualizes CA County shoreline miles as a crude proxy for risk of sea-level rise,
   assuming that more shoreline miles equals more risk
   It uses pandas and matplotlib to create a bar chart data visualization that shows shoreline miles by county.
   <br />&nbsp;<br />

4. **econ_impact_ocean_sector_gdp.ipynb**<br />
   The aim of this program is to extract datapoints from PDF files hosted at the API endpoint, and
   create a pie chart data visualization to represent ocean sector GDP by CA County.
   It is a work in progress that successfully extracted the text from a PDF file using the PyPDF2 module,
   and the start of using regular expressions to save the datapoint percentages into a Python dictionary.
   A manual Python dictionary is also included, but work is still needed here to process the data and
   produce the data visualization.
   <br />&nbsp;<br />

## 4. Conclusion

It's difficult to make any definitive conclusions about which county or counties are
most at risk from sea-level change, given the limited amount of data gathered and visualized,
with key data points from the PDF such as population at risk to 100 year flood, and potential bluff erosion
impact on property not included.

<p>Based on the data visualized, it can be tentatively concluded that southern California counties in general seem
to be at higher risk, as they scored high on the risk factor totals and the percentage of ocean sector GDP,
while shoreline miles do not seem to be a good proxy for risk by themselves.</p>

<p>Technical conclusions include the takeaway that the Python programming language is well positioned for this kind of 
data analysis, with modules to access APIs, do File I/O, and quickly process and visualize data.</p>

## 5. Python programs

### Key files included in the project zip file include 3 Jupyter Notebook files and 1 .py utility file <br />

(also included in the bundle is a requirements.txt file and a pdf file used for File I/O)

- api_data_utils.py
- ccc_risk_factors.ipynb
- shoreline_miles_as_risk_proxy.ipynb
- econ_impact_ocean_sector_gdp.ipynb

## Appendix A: References

Correct way to try/except using Python requests module?

https://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module
