# 📌 MISP Basics Documentation

## 🔹 What is MISP?
MISP (Malware Information Sharing Platform) is an open-source threat intelligence platform designed to store, share, and analyze threat indicators such as malware, phishing, and attack patterns.

---

## 📌 MISP Installation

### 🔹 Prerequisites
- Ubuntu 20.04+ / Debian 11+
- Minimum **4GB RAM**, **2 CPUs**
- MySQL / MariaDB
- Python 3.6+
- Redis

### 🔹 Install MISP on Ubuntu
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install -y curl gnupg2 unzip redis-server mariadb-server python3 python3-pip

# Clone MISP repo
cd /var/www/
sudo git clone https://github.com/MISP/MISP.git
cd MISP
sudo git submodule update --init --recursive
```

### 🔹 Start Services
```bash
sudo systemctl restart apache2
sudo systemctl restart mariadb
sudo systemctl enable --now redis-server
```

---

## 📌 MISP API Basics

### 🔹 Authentication
- Generate API Key: `Administration > List Auth Keys > Add API Key`
- Use API Key in headers:
```bash
curl -X GET "http://<misp-url>/events" \
     -H "Authorization: <your-api-key>" \
     -H "Accept: application/json"
```

### 🔹 Fetching Events
```python
import requests

misp_url = "http://<misp-url>"
api_key = "<your-api-key>"

headers = {
    "Authorization": api_key,
    "Accept": "application/json"
}

response = requests.get(f"{misp_url}/events", headers=headers)
print(response.json())
```

### 🔹 Adding an Event
```python
event_data = {
    "Event": {
        "info": "Suspicious IP detected",
        "attribute_count": 1,
        "threat_level_id": 3,
    }
}

response = requests.post(f"{misp_url}/events/add", headers=headers, json=event_data)
print(response.json())
```

---

## 📌 MISP Data Structure

### 🔹 Key Components
- **Events**: Containers for related threat data  
- **Attributes**: Individual IOCs (IPs, hashes, domains)  
- **Objects**: Grouped attributes (e.g., file objects contain filename, hash, size)  
- **Tags**: Labels for classification (TLP, MITRE ATT&CK)  
- **Galaxy**: Predefined threat intelligence (APT groups, malware families)  


## 📌 Useful MISP Commands

### 🔹 List MISP Users
```bash
mysql -u misp -p -e "SELECT id, email FROM users;" misp
```

### 🔹 Restart MISP Services
```bash
sudo systemctl restart apache2
sudo systemctl restart mysql
sudo systemctl restart redis-server
```

---

## 📌 MISP Resources
- 📖 [MISP GitHub](https://github.com/MISP/MISP)  
- 📖 [MISP Documentation](https://www.circl.lu/doc/misp/)  
- 📖 [MISP API Docs](https://misp.github.io/MISP/)  

---

