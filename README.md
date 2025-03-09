# **Threat Intelligence Correlation using MISP, Nessus and NVD.**

## **Overview**
This repository provides a comprehensive guide on correlating threat intelligence data from MISP (Malware Information Sharing Platform), Nessus Scan Reports, and NVD (National Vulnerability Database). It focuses on threat intelligence analysis, Elasticsearch integration, and non-SIEM-based correlation techniques to identify vulnerabilities associated with known threat indicators. The repository includes step-by-step instructions, scripts, and documentation to assist cybersecurity professionals in enhancing threat detection and vulnerability assessment.

## **Features**
✅ README2 file guides you on uploading a file to Elasticsearch.  

✅ Project file guides you on how you can achieve correlation without the use of a SIEM tool.

✅ Misp basics file consists of basics of Misp. 

✅ Misp and NVd file guides you on achieving correlation between misp and nvd using Elasticsearch. 


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
