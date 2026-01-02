DoS Attack Simulation Tool (Educational)
📌 Overview

This project is a Denial-of-Service (DoS) attack simulation tool written in Python.
It is designed strictly for educational purposes, such as:

Learning about multithreading

Understanding how request floods work

Testing your own servers or authorized environments

Practicing configuration-driven programs

The program sends multiple HTTP GET requests to a target URL using a configurable number of threads.

📁 Project Structure
.
├── main.py              # Entry point of the application
├── DoS_Attack.py        # Core DoS simulation logic
├── Config.conf          # Configuration file
└── README.md            # Project documentation

⚙️ How It Works

main.py

Loads configuration from Config.conf

Handles errors and execution timing

Starts the DoS simulation

DoS_Attack.py

Creates a thread pool using ThreadPoolExecutor

Each thread sends multiple HTTP requests

Tracks successful and failed requests

Prints a summary at the end

Config.conf

Defines the target URL

Sets the number of threads

Sets how many requests each thread sends

🧾 Configuration (Config.conf)
[settings]

TARGET_URL = https://www.google.com/
NUM_THREADS = 100
REQUESTS_PER_THREAD = 100

Configuration Options
Setting	Description
TARGET_URL	The URL to send requests to
NUM_THREADS	Number of concurrent threads
REQUESTS_PER_THREAD	Requests sent per thread

⚠️ Only test URLs you own or have permission to test.

▶️ How to Run
1. Install Dependencies
pip install requests

2. Run the Program
python main.py

📊 Output Example
Starting simulation: 100 threads, 100 reqs/thread...
Target: https://www.google.com/

--- Simulation Summary ---
Total Requests Attempted: 10000
Successful (2xx):       10000
Failed:                 0

Total simulation time: 5.42 seconds.

❗ Important Disclaimer

🚨 LEGAL & ETHICAL WARNING

This tool is provided for educational purposes only.

Do NOT use this tool against:

Public websites

Servers you do not own

Systems without explicit permission

Unauthorized DoS attacks are illegal and may result in:

Criminal charges

Academic penalties

Civil liability

The author assumes no responsibility for misuse.

🧠 Concepts Demonstrated

Multithreading with ThreadPoolExecutor

HTTP requests using requests

Configuration files (configparser)

Error handling

Performance measurement
