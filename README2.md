# Correlation Steps for Uploading Nessus and MISP Data to Elasticsearch

## Step 1: Convert Nessus File to JSON Bulk Format

The following Python script converts a Nessus scan file (`.nessus`) into a bulk JSON format for Elasticsearch.

### **Script:**

```python
import json
import xml.etree.ElementTree as ET

# File paths
nessus_file = "/home/musharaf-misp-admin/musharaf/misp_scan_f20myj.nessus"
bulk_output = "/home/musharaf-misp-admin/musharaf/nessus_bulk.json"  # ✅ Fixed

try:
    tree = ET.parse(nessus_file)
    root = tree.getroot()

    bulk_data = ""
    index_name = "nessus_scans"

    for report in root.findall(".//ReportHost"):
        ip = report.get("name")
        for item in report.findall(".//ReportItem"):
            cve = item.get("cve") if item.get("cve") else "Unknown"
            severity = item.get("severity") if item.get("severity") else "Low"

            bulk_data += json.dumps({"index": {"_index": index_name}}) + "\n"
            bulk_data += json.dumps({"ip": ip, "cve": cve, "severity": severity}) + "\n"

    if bulk_data:
        with open(bulk_output, "w") as f:
            f.write(bulk_data)
        print(f"✅ Bulk JSON saved to {bulk_output}")
    else:
        print("❌ No data extracted from Nessus file.")

except ET.ParseError as e:
    print(f"❌ XML Parsing Error: {e}")
except FileNotFoundError:
    print(f"❌ File not found: {nessus_file}")
except Exception as e:
    print(f"❌ Unexpected error: {e}")
```

---

## Step 2: Convert MISP Event (STIX 2.0) to JSON Bulk Format

Use the following script to transform a MISP event in STIX 2.0 format into Elasticsearch bulk format.

### **Command:**

```bash
python3 - <<EOF
import json

# File paths
input_file = "/home/musharaf-misp-admin/musharaf/misp scan_f20myj.nessus"
output_file = "/home/musharaf-misp-admin/nessus_cve_bulk.json"

# Load the original JSON file
with open(input_file, "r", encoding="utf-8") as file:
    data = json.load(file)

# Extract CVE data
cve_list = data.get("vulnerabilities", [])

# Convert to Elasticsearch bulk format
bulk_data = ""
for item in cve_list:
    cve = item.get("cve", {})
    cve_id = cve.get("id", "UNKNOWN")
    bulk_data += json.dumps({"index": {"_index": "nvd_cve_index", "_id": cve_id}}) + "\n"
    bulk_data += json.dumps(cve) + "\n"

# Save to bulk file
with open(output_file, "w", encoding="utf-8") as bulk_file:
    bulk_file.write(bulk_data)

print(f"Bulk data saved to {output_file}")
EOF
```

After execution, the bulk data will be saved to:

```
/home/musharaf-misp-admin/nvd_cve_bulk.json
```

---

## Step 3: Upload Bulk Data to Elasticsearch

Once the Nessus and MISP files are converted into bulk JSON format, use the following **cURL** commands to upload them to Elasticsearch.

### **Upload Nessus Data:**

```bash
curl -u elastic:"wlt8i+2TdnvX0dn-EBES" -X POST "https://localhost:9200/_bulk" \
     -H "Content-Type: application/json" --data-binary @/home/musharaf-misp-admin/musharaf/nessus_bulk.json -k
```

### **Upload MISP Data:**

```bash
curl -u elastic:"wlt8i+2TdnvX0dn-EBES" -X POST "https://localhost:9200/_bulk" \
     -H "Content-Type: application/json" --data-binary @/home/musharaf-misp-admin/musharaf/misp_bulk.json -k
```

Once both files are uploaded, the Nessus and MISP event data will be stored in Elasticsearch for further analysis and correlation in Kibana.



