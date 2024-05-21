# BalanceReporter

BalanceReporter is a prototype of Python application designed to generate balance reports from various financial data sources. This repository contains the source code and necessary configurations to set up and run the application.
Application consist of 3 services: Orchestrator, Calculator and ReportMaker

## Features

- Fetches and processes financial data
- Generates comprehensive balance reports
- Supports various data formats
- Save report to AWS S3 bucket

## Technologies Used

- Python
- AWS S3, SQS

## Getting Started

### Prerequisites

- Python 3.8+ installed
- Required Python packages (listed in `requirements.txt`)

### Installation

1. Clone the repository:
   git clone https://github.com/Newtonn00/BalanceReporter.git
2. Install the required dependencies
   pip install -r requirements.txt
3. Setup information in settings.ini   
4. Run 3 services:
   python calc_main.py
   python main.py
   python report_maker_main.py
   

