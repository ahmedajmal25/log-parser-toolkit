# 🧪 Log Parser Toolkit

A Python-based log parsing toolkit that uses **OOP**, **regular expressions**, and **generators** to efficiently analyze log files. Designed to simulate real-world system log testing (e.g., automotive or embedded systems).

---

## 🚀 Features

- 🔍 Parse logs using regular expressions
- 🏗️ Clean class structure using Object-Oriented Programming
- 🧮 Count log levels (`INFO`, `WARNING`, `ERROR`, etc.)
- 🔎 Filter logs by level
- 🔎 Filter logs by message
- 💾 Export parsed logs to CSV
- 🧠 Handles large files with generators
- ✅ Unit tested with `unittest`

---

## 📂 Project Structure

```
log_toolkit/
├── main.py             # Main script to run the parser
├── log_parser.py       # Contains the LogParser class and logic
├── sample_log.txt      # Sample log file for testing
├── test_log_parser.py  # Unit tests using unittest
└── README.md           # This documentation file
```

---

## 🛠️ Requirements

- Python 3.7 or later  
- No external libraries required (uses built-in Python modules)

---

## ▶️ How to Run

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/log-parser-toolkit.git
cd log-parser-toolkit
```

### ▶️ 2. Run the Parser

```bash
python3 main.py
```

### ✅ 3. Run Unit Tests

```bash
python3 test_log_parser.py
```

---

## 📁 Sample Output

### 📝 Log Summary:
```
 - INFO: 2 entries
 - WARNING: 1 entries
 - ERROR: 2 entries
```

### 🔍 Detailed Entries:
```
[2025-04-11 14:23:10] INFO - System started successfully.
[2025-04-11 14:24:45] WARNING - High memory usage detected.
...
```

### 📁 Exported File:
The filtered or unfiltered log entries are exported to `log_output.csv`.

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the toolkit.

---

## 📧 Contact

For questions or feedback, please contact [your_email@example.com].