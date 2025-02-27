import json
import xml.etree.ElementTree as ET

# File paths (Fixed missing quote)
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

