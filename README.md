# **Threat Intelligence Correlation using MISP, Nessus and NVD**

## **Overview**
This repository contains a Jupyter Notebook (`project.ipynb`) that performs correlation between threat intelligence data from **MISP** (Malware Information Sharing Platform), **Nessus Scan Reports**, and **NVD** (National Vulnerability Database). The project helps in identifying vulnerabilities associated with known threat indicators.

## **Features**
✅ README2 file guides you on how you can upload file to elastic search  

✅ Projest file guides you on how you can achieve correlation without the use of siem tool

✅ Misp basics file consists of basics of misp. 

✅ Misp and NVd file guides you on how to achieve correlation between mis[ pand nvd using ellasticsearch. 


## **Project.ipynb Code Breakdown**
This project contains three Python scripts inside the Jupyter Notebook:

1. **MISP CVE Extraction**:  
   - Fetches threat intelligence data from MISP.  
   - Extracts CVEs associated with threats.  
   
2. **Nessus Scan CVE Extraction**:  
   - Parses Nessus vulnerability scan reports.  
   - Extracts CVE IDs found in the scan results.  

3. **Threat Intelligence Correlation**:  
   - Matches extracted MISP CVEs with Nessus scan results.  
   - Queries the **NVD API** to fetch detailed vulnerability information.  
   - Stores and visualizes results using **Elasticsearch & Kibana**.  

## **Installation**
1. **Clone this repository**  
   ```bash
   git clone https://github.com/musharafmaqbool/MISP-and-NESSUS-SCAN-CORRELATION.git
