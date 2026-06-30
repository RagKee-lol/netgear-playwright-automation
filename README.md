# Netgear WiFi Automation using Playwright

A Python automation framework built using **Playwright**, **Pytest**, and the **Page Object Model (POM)** to automate wireless network configuration on the Netgear Insight Cloud Portal.

## Features

- Automated login to Netgear Insight Portal
- Navigate to Wireless Settings
- Create new SSIDs
- Configure SSID Password
- Select Operating Mode (Bridge / NAT)
- Configure NAT Mode
- Enable or Disable WiFi Bands
  - 2.4 GHz
  - 5 GHz
- Select Security Mode
  - Open
  - WPA2 Personal
  - WPA2 Personal Mixed
  - WPA3 Personal
  - WPA3 Personal Mixed
  - WPA3 Enterprise
- Verify SSID creation
- Generate HTML Test Reports using pytest-html

---

## Tech Stack

- Python 3
- Playwright
- Pytest
- pytest-html
- Page Object Model (POM)

---

## Project Structure

```
netgear_automation/
│
├── pages/
│   ├── login_page.py
│   ├── dashboard_page.py
│   └── wireless_page.py
│
├── tests/
│   └── test_create_ssid.py
│
├── utils/
│   └── config.py
│
├── reports/
│
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/netgear-automation.git

cd netgear-automation
```

Install dependencies

```bash
pip install -r requirements.txt
```

Install Playwright browsers

```bash
playwright install
```

---

## Configuration

Update your credentials inside `config.py`

```python
USERNAME = "your_username"
PASSWORD = "your_password"

SSID_NAME = "TestSSID"
SSID_PASSWORD = "Password123"
```

> Do **not** commit real credentials to GitHub.

---

## Running the Test

Run the complete automation:

```bash
pytest tests/test_create_ssid.py
```

Generate an HTML report

```bash
pytest tests/test_create_ssid.py --html=reports/report.html --self-contained-html
```

---

## Test Workflow

```
Login
      ↓
Select Organization
      ↓
Select Location
      ↓
Open Wireless Settings
      ↓
Create SSID
      ↓
Choose NAT / Bridge Mode
      ↓
Configure WiFi Band
      ↓
Configure Security
      ↓
Save Settings
      ↓
Verify SSID Creation
```

---

## Skills Demonstrated

- Playwright Automation
- Python Programming
- Page Object Model
- UI Test Automation
- Web Element Inspection
- Locator Strategies
- HTML Report Generation
- Test Framework Design
- Automation Debugging

---

## Future Improvements

- Data-driven testing
- Parallel execution
- GitHub Actions CI/CD
- Screenshot capture on failure
- Logging improvements
- Multiple browser support
- Delete/Edit SSID automation
- Environment variable support for credentials

---

## Author

**Keertana K**

Automation Framework built as part of an internship project using Playwright and Python.
