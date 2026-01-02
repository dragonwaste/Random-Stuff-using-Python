# DoS Attack Simulation Tool (Educational)

## 📌 Overview

This project is a **Denial-of-Service (DoS) attack simulation tool** developed in Python.  
It is intended **strictly for educational and learning purposes**, including:

- Exploring multithreading concepts  
- Understanding how request flooding impacts servers  
- Testing systems you own or have explicit authorization to test  
- Practicing configuration-based program design  

The application generates multiple HTTP GET requests to a specified target URL using a configurable number of threads.

---

## 📁 Project Structure

.
├── main.py              # Main entry point of the program  
├── DoS_Attack.py        # Implements the DoS simulation logic  
├── Config.conf          # Configuration settings  
└── README.md            # Project documentation  

---

## ⚙️ How the Program Works

### main.py

- Reads settings from `Config.conf`  
- Handles configuration and runtime errors  
- Measures execution time  
- Starts the DoS simulation process  

### DoS_Attack.py

- Uses `ThreadPoolExecutor` to manage multiple threads  
- Each thread sends a defined number of HTTP requests  
- Counts successful and failed requests  
- Displays a summary after execution  

### Config.conf

- Specifies the target URL  
- Defines the number of threads  
- Sets the number of requests per thread  

---

## 🧾 Configuration (Config.conf)

```ini
[settings]

TARGET_URL = https://www.google.com/
NUM_THREADS = 100
REQUESTS_PER_THREAD = 100
```

