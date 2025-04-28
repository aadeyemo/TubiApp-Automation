# 📱 TubiApp Automation - Android Mobile UI Test

> Automated end-to-end testing project for the Tubi Android App using Appium, Python, and Pytest.

---

## 🚀 Project Highlights

- Bypasses onboarding on Tubi app.
- Navigates to **Movies > Family Movies** category.
- Searches and verifies the asset: **"UglyDolls"**.
- Generates a beautiful **HTML test report**.
- Runs tests both locally and with **GitHub Actions CI**.

---

## 🧩 Tech Stack

| Component           | Version / Framework |
|---------------------|----------------------|
| Appium Server        | 2.17.1               |
| Appium Python Client | 2.11.0               |
| Pytest               | 8.1.1                |
| Pytest-HTML          | 4.0.2                |
| Android Real Device  | UMIDIGI A7S          |

---

## 🗂 Project Structure

```bash
TubiApp-Automation/
├── tubiapp/
│   ├── conftest.py          # Fixtures: Driver setup
│   ├── pages/
│   │   ├── home_page.py     # Home page actions
│   │   └── search_page.py   # Search page actions
│   ├── tests/
│   │   └── test_search_movie.py # Main test cases
│   └── utils/
│       └── recorder.py      # Screen recorder utilities
├── requirements.txt         # Python dependencies
├── pytest.ini                # Pytest configuration
├── README.md                 # Project Documentation
├── .github/
│   └── workflows/
│       └── tests.yml         # GitHub Actions CI workflow
└── reports/                  # Test reports (auto-generated)
