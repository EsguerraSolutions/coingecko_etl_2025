# CryptoPipe - Cryptocurrency Hybrid ETL-ELT Data Pipeline

<p align="center">
  <strong>Production-style end-to-end hybrid ETL-ELT data pipeline with live visualization built on a cryptocurrency API</strong>
</p>

<p align="center">
  <a href="#live-visualization">Live Visualization</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#data-testing">Data Testing</a> •
  <a href="#architecture">Architecture</a> •
  <a href="#project-structure">Project Structure</a> •
  <a href="#roadmap">Roadmap</a> •
  <a href="#acknowledgments">Acknowledgments</a> •
  <a href="#contact">Contact</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/SQL-25A1D5?logo=postgresql&logoColor=white" alt="SQL"/>
  <img src="https://img.shields.io/badge/Apache%20Spark-E25A1C?logo=apachespark&logoColor=white" alt="Spark"/>
  <img src="https://img.shields.io/badge/dbt-FF694B?logo=dbt&logoColor=white" alt="dbt"/>
  <img src="https://img.shields.io/badge/BigQuery-4285F4?logo=googlebigquery&logoColor=white" alt="BigQuery"/>
  <img src="https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/React-61DAFB?logo=react&logoColor=black" alt="React"/>
  <img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License"/>
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen" alt="PRs Welcome"/>
</p>

---

## 🥯 What is CryptoPipe?

CryptoPipe is a **production-style end-to-end hybrid ETL-ELT data pipeline** that is designed to give crypto enthusiasts a reliable way to review, monitor, and understand market trends using updated and historical data. It showcases how raw API data can be ingested, cleaned, transformed, stored in a data warehouse, and visualized into actionable insights. The project demonstrates practical data engineering concepts—from orchestration to automation—while providing a transparent, reproducible framework for anyone wanting to explore the crypto market through a modern data stack.

### Perfect For

- 🔥 **Crypto Enthusiasts** - People who want to explore real-time and historical price movements and understand market trends
- 📈 **Crypto Traders** - Active traders who need timely, reliable market data to inform buy/sell decisions
- 👨‍💻 **Crypto Application Developers** - Engineers who plan to integrate crypto market data into their apps or automate their own data pipelines.
- 👩🏻‍🔬 **Crypto Data Analysts** - Analysts who want structured, clean data for deeper insights, charts, and performance tracking.
- 👨🏻‍💻 **Data Engineers** - Engineers interested in studying the architecture of a complete ETL/ELT pipeline with orchestration and cloud warehousing.
- 🕵🏼‍♂️ **Quantitative Researchers** - Individuals analyzing price behavior, volatility, or building algorithmic strategies who benefit from clean, historical datasets.
- 💲 **Finance & Trading Enthusiasts** - Users who want intuitive visual dashboards to track, compare, and understand cryptocurrency performance over time.

### Key Features

- **🧹 Data Cleaning & Standardization** - Cleans, validates, and structures raw API data into analytics-ready formats.
- **🧩 Hybrid ETL + ELT Architecture** - Combines Python-based preprocessing with dbt warehouse transformations.
- **📦 BigQuery Warehousing** - Stores cleaned data in a scalable, cloud-based analytics warehouse.
- **🖇️ Idempotent Pipeline Logic** - Ensures safe re-runs without duplicating or corrupting data.
- **🥇 Medallion Architecture** - Organizes data into Bronze, Silver, and Gold stages for clarity and maintainability.
- **🔄 dbt Transformation Layer** - Applies modular SQL transformations with documentation and lineage tracking.
- **📊 Interactive Visualization** - Delivers insights through a visual table for easy trend analysis.
- **🔀 Derived Feature Columns** - Generates additional calculated metrics (e.g., percentage change, moving averages) to enhance analysis and visualization.
- **🎬 Production-Inspired Practices** - Implements real-world engineering patterns across ingestion, storage, and transformation.

---

## 🗃️ Source of Data

This project uses cryptocurrency market data sourced from the [CoinGecko API](https://www.coingecko.com/en/api), a widely trusted platform that provides free and reliable real-time and historical crypto data. The API is queried during the ingestion stage, ensuring the pipeline consistently processes accurate and up-to-date crypto market information for downstream cleaning, modeling, warehousing, and visualization.

_(COMING SOON)_ Additional data sources are planned to be integrated in future updates.

---

<h2 id="live-visualization"> ▶️ Live Visualization </h2>

For a quick live demo of the visualization page integrated with the project's working API, visit the [CryptoPipe Live Visualization](https://crypto-frontend-2025.vercel.app/).

---

<h2 id="quick-start"> 🚀 Quick Start </h2>

### Prerequisites

- Python 3.10+
- Google Cloud / BigQuery Account _(Required to load datasets, tables, and enable the BigQuery API)_
- BigQuery Service Account Key _(Used by the pipeline for programmatic access of FastAPI)_
- CoinGecko API Key _(Required for CoinGecko demo/pro endpoints)_

### 1. Clone and Setup

```bash
git clone https://github.com/EsguerraSolutions/coingecko_etl_2025.git

# Create virtual environment
python3.11 -m venv .venv
source activate.sh

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
# Copy example env file
cp templates/.env.example env.text

# Edit .env with following data:
# - CoinGecko API key and URL (for data extraction)
# - BigQuery datasets, tables and Service Account Key (for loading into BigQuery and serving into FastAPI)
# - Frontend URL (for CORS, to allow cross-origin requests)
```

### 3. Configure profiles.yml

```bash
# Copy the contents of the sample profiles.example.yml file to your clipboard

## Windows
cat templates/profiles.example.yml | clip

## macOS
cat templates/profiles.example.yml | pbcopy

## Linux (if needed)
cat templates/profiles.example.yml | xclip -selection clipboard

# After copying, go to your .dbt folder and paste the content into your profiles.yml file.
```

### 4. Run ETL-ELT Pipeline Scripts

```bash
# Run data extraction and ingestion, cleaning with PySpark, loading into BigQuery, and dbt transformations
python scripts/run_etl.py
```

### 5. Run the Server with Uvicorn

```bash
# Run the API locally for testing and development
uvicorn server.api:app --reload
```

---

<h2 id="data-testing"> 🔬 Data Testing </h2>

Additional data validation tests are available in two different ways:

### 1. Run the notebooks under the `checking_notebooks` directory, built using PySpark.

_(COMING SOON)_ Logging of inconsistent records identified by the PySpark validation scripts.

### 2. Run the dbt tests:

```bash
dbt test --project-dir dbt
```

---

<h2 id="architecture"> 🏛️ Architecture </h2>

```
 ┌─────────────────────┐
 │                     │
 │  Source Crypto API  │
 │                     │
 └──────────┬──────────┘
 (Python)   │
Extraction  │
Ingestion   │
            ▼
       ┌─────────┐
       │  Bronze │
       └────┬────┘
  (PySpark) │
  Checking  │
  Cleaning  │
            ▼
       ┌─────────┐
       │  Silver │
       └────┬────┘
 (BigQuery) │
 Loading    │
 ┌───────────────────────────────────────────────────────┐
 │          │               Gold                         │
 │          ▼          Data Warehouse                    │
 │     ┌─────────┐        ┌──────┐        ┌───────────┐  │
 │     │ Staging ├───────►│ Core ├───────►│ Analytics │  │
 │     └─────────┘        └───┬──┘        └───────┬───┘  │
 │                 (dbt)      │   (dbt)           │      │
 │               Modelling    │   Transformation  │      │
 │                            ▼                   │      │
 │     ┌────────────┐    ┌───────┐                │      │
 │     │ Dimensions │◄───┤ Facts │                │      │
 │     └────────────┘    └───────┘                │      │
 └───────────────────────────────────────────────────────┘
                                                  │
                                 Serve with API   │
                                                  ▼
                                            ┌─────────┐
                                            │ FastAPI │
                                            └─────┬───┘
                                 API Integration  │
                                                  ▼
                                             ┌───────┐
                                             │ React │
                                             └───────┘
```

**Tech Stack:**

- **Scripts:** Python
- **Server:** FastAPI
- **Data Warehouse:** BigQuery
- **Cleaning:** PySpark
- **Transformation:** dbt
- **Frontend:** React
- **Orchestration:** Airflow _(coming soon)_
- **Server Deployment:** Render
- **Frontend Deployment:** Vercel

---

<h2 id="project-structure"> 🏗️ Project Structure </h2>

```
coingecko_etl_2025/
├── checking_notebooks/  # Jupyter Notebooks for manual validation of data
├── data/                # Storage directory of .parquet and .json files
├── dbt/                 # Directory of dbt models, tests and snapshots
├── logs/                # For future update, logging of inconsistent data
├── notebooks/           # PySpark transformations on Jupyter notebooks for developer's exploration
├── pipelines/           # PySpark transformations on ready to run scripts
├── readers/             # PySpark functions to read data from parquet files
├── schema/              # Definition of schema
├── scripts/             # BigQuery scripts and master script to run ETL processes
├── server/              # FastAPI Server directory
├── templates/           # Ready made templates for setting up the environment
└── utils/               # Utility functions used across the pipelines
```

---

<h2 id="roadmap"> 🗺️ Roadmap </h2>

Planned future updates

- **Airflow orchestration** - Add Apache Airflow to automate, schedule, and monitor the full ETL–ELT workflow.
- **Additional data sources** - Integrate more crypto data providers to enrich and validate market insights.
- **Logging of bad data** - Implement data-quality checks and logging to detect and isolate malformed or inconsistent records.
- **Error handling** - Add structured error handling to make pipeline execution more stable, predictable, and recoverable.

---

<h2 id="acknowledgments"> 🙏 Acknowledgments </h2>

Special thanks to the tools, platforms, and learning resources that supported the development of this project:

- [CoinGecko API](https://www.coingecko.com/en/api) - for providing free and reliable cryptocurrency market data
- Python, PySpark, FastAPI, dbt, and Airflow - open-source technologies powering ingestion, processing, API development, and orchestration.
- [Google BigQuery](https://cloud.google.com/bigquery) - for scalable and efficient data warehousing
- [React](https://react.dev/) - for enabling the interactive and responsive visualization interface.
- [Vercel](https://vercel.com/) - for providing fast and seamless frontend hosting and deployment.
- [Render](https://render.com/) - for free hosting and serving the API backend with ease.
- Open-source community - for documentation, libraries, and shared knowledge.
- Data Engineering YouTube Channels - such as [Ansh Lamba](https://www.youtube.com/@AnshLambaJSR), [Data with Baraa](https://www.youtube.com/@DataWithBaraa) and [CK Data Tech](https://www.youtube.com/channel/UCYg2Xa699XhuDwl3n5M8W-w), whose content supported my learning journey.

---

<h2 id="contact"> 📩 Contact </h2>

- **GitHub:** [@esguerrasolutions](https://github.com/EsguerraSolutions)
- **LinkedIn:** [Jonathan Esguerra](https://www.linkedin.com/in/esguerrasolutions/)
- **Email:** esguerradesign@gmail.com

---

<p align="center">
  <sub>Built to provide clean and reliable crypto data with more analytical features</sub>
</p>
