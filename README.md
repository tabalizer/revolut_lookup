# Revolut Lookup

A simple Python command-line tool to fetch public Revolut user profiles using their API.

## 🚀 Features

- Enter any Revolut username and fetch associated public profile data.
- Lightweight, fast, and easy to use.
- Outputs raw API response (JSON or HTML, depending on the username).

## 📦 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/revolut_lookup.git
cd revolut_lookup
```

### Step 2: Set Up a Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Required Python Packages

```bash
pip install -r requirements.txt
```

## ▶️ How to Use

Run the script with:

```bash
python revolut_lookup/main.py
```

You'll be asked to input a Revolut username. The tool will then contact the public API:

```
https://revolut.me/api/web-profile/<USERNAME>
```

and display the result in your terminal.

### Example Output

```bash
Enter Revolut username: johndoe
API Response:
{
  "name": "John Doe",
  "profile": "https://revolut.me/johndoe",
  ...
}
```

## 🗂️ Project Structure

```
revolut_lookup/
├── revolut_lookup/
│   ├── __init__.py
│   └── main.py
├── requirements.txt
├── setup.py
├── README.md
├── .gitignore
└── venv/ (optional – do not upload this to GitHub)
```

## ⚙️ Dependencies

- Python 3.6 or newer
- `requests` (listed in `requirements.txt`)

## 🛠 Setup for Development

To install the package locally for development:

```bash
pip install -e .
```

## 🐙 GitHub Deployment

To push this project to GitHub:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/revolut_lookup.git
git push -u origin main
```

## 📜 License

This project is open-sourced under the MIT License.
