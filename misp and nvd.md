# 📌 MISP & NVD CVE Correlation Documentation

## 🔹 What is MISP?

MISP (Malware Information Sharing Platform) is an open-source threat intelligence platform designed to store, share, and analyze threat indicators such as malware, phishing, and attack patterns.

## 🔹 What is NVD?

The National Vulnerability Database (NVD) is a repository of vulnerability management data that includes CVE (Common Vulnerabilities and Exposures) entries, used to identify security risks in software and hardware.

---

## 📌 Correlating MISP with NVD CVEs

### 🔹 Prerequisites

- Ubuntu 20.04+ / Debian 11+
- Minimum **4GB RAM**, **2 CPUs**
- MySQL / MariaDB
- Python 3.6+
- Redis
- Elasticsearch & Kibana (for visualization)

### 🔹 Fetching MISP Events in STIX Format

```bash
curl -X GET "http://<misp-url>/events/restSearch" \
     -H "Authorization: <your-api-key>" \
     -H "Accept: application/json" \
     -d '{"returnFormat": "stix2"}'
```

### 🔹 Fetching CVEs from NVD API

```bash
curl -s "https://services.nvd.nist.gov/rest/json/cves/2.0?resultsPerPage=500" | jq '.' > nvd_cves.json
```

### 🔹 Formatting NVD Data for Elasticsearch

```python
import json

def format_nvd_cves(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as file:
        data = json.load(file)
    cve_list = data.get("vulnerabilities", [])
    bulk_data = ""
    for item in cve_list:
        cve = item.get("cve", {})
        cve_id = cve.get("id", "UNKNOWN")
        bulk_data += json.dumps({"index": {"_index": "nvd_cve_index", "_id": cve_id }}) + "\n"
        bulk_data += json.dumps(cve) + "\n"
    with open(output_file, "w", encoding="utf-8") as bulk_file:
        bulk_file.write(bulk_data)
    print(f"Bulk data saved to {output_file}")

format_nvd_cves("nvd_cves.json", "nvd_cve_bulk.json")
```

### 🔹 Uploading Data to Elasticsearch

```bash
curl -X POST "http://localhost:9200/nvd_cve_index/_bulk" -H "Content-Type: application/json" --data-binary @nvd_cve_bulk.json
```

---

## 📌 Performing Correlation in Kibana

### 🔹 Extract CVEs from MISP

```bash
GET misp_cves/_search
{
  "size": 1000,
  "_source": ["name"],
  "query": {
    "match_all": {}
  }
}
```

### 🔹 Search for a Specific CVE in NVD

```bash
GET nvd_cve_index/_search
{
  "size": 1,
  "query": {
    "terms": {
      "id.keyword": ["CVE-2024-1234"]
    }
  }
}
```

### 🔹 Performing CVE Correlation

```python
def correlate_cves(misp_cves, nvd_cves):
    common_cves = misp_cves.intersection(nvd_cves)
    print("Correlated CVEs:")
    for cve in common_cves:
        print(cve)

misp_cves = {"CVE-2024-1234", "CVE-2024-5678"}
nvd_cves = {"CVE-2024-1234", "CVE-2024-9101"}
correlate_cves(misp_cves, nvd_cves)
```

---

## 📌 Useful Resources
- 📖 [MISP GitHub](https://github.com/MISP/MISP)
- 📖 [MISP Documentation](https://www.circl.lu/doc/misp/)
- 📖 [NVD CVE Database](https://nvd.nist.gov/)
- 📖 [Elasticsearch Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)

---

