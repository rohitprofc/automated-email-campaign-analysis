# Automated Email Campaign Analysis

This project provides a Python script to analyze email campaign data and generate reports in Excel. The analysis includes summary statistics, open rates over time, click-through rates over time, and open rates by segment.

## Project Structure

```
.
├── email_campaign_data.csv    # Sample email campaign data
├── email_campaign_analysis.py # Main script for data analysis and report generation
├── open_rates_over_time.png   # Open rates over time plot
├── ctr_over_time.png          # Click-through rates over time plot
├── open_rates_by_segment.png  # Open rates by segment plot
└── README.md                  # Project documentation
```

## Prerequisites

- Python 3.x
- pandas
- matplotlib
- seaborn
- openpyxl

You can install the required packages using pip:

```sh
pip install pandas matplotlib seaborn openpyxl
```

## Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/rohitprofc/automated-email-campaign-analysis.git
   cd automated-email-campaign-analysis
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Generate Sample Data**:
   ```bash
   python data_generate.py
   ```

4. **Run the analysis**:
   ```bash
   Run all cells in analyze_campaigns.ipynb
   ```

## The script will generate the following output files:

- `email_campaign_report.xlsx`: Excel report containing raw data, summary statistics, and analysis results.
- `open_rates_over_time.png`: Line plot of open rates over time.
- `ctr_over_time.png`: Line plot of click-through rates over time.
- `open_rates_by_segment.png`: Bar plot of open rates by segment.
