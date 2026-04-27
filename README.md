# Nillion MPC vs Azure Baseline Benchmark

This repository contains the code for benchmarking a blind auction execution time. It compares running the auction logic locally/in a traditional cloud environment (Azure) against running it in a Trusted Execution Environment (TEE) using Nillion's nilCC (AMD SEV-SNP).

## Prerequisites
* Python 3.9+
* Docker (Optional, for deploying the API)

## Local Setup & Installation

Install the required Python libraries for the web server (FastAPI/Uvicorn) and the benchmarking client (Requests):


### Install requirements
```bash
pip install fastapi uvicorn requests
```

## Start the server locally
```bash
uvicorn main:app --reload
```

## Run the benchmark
### Standard (100 bids, 100 iterations)
python3 benchmark.py

### Custom (t.ex. 1000 bids, 10 iterations)
python3 benchmark.py 1000 10