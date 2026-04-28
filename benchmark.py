import sys
import time
import random
import requests
from statistics import mean

#Local: http://127.0.0.1:8000/auction
#GCP: http://34.51.252.139/8000/auction

SERVER_URL = "http://34.51.252.139/8000/auction"

# Function to generate synthetic bids
def generate_synthetic_bids(num_bidders):
    """Generates a list of dictionaries containing random bids."""
    bids = []
    for i in range(num_bidders):
        bids.append({
            "bidder_id": f"Party_{i+1}",
            "bid_amount": random.randint(100, 10000)
        })
    return bids

def run_network_benchmark(num_bidders, iterations):
    times = []
    
    print(f"Run network-benchmark mot {SERVER_URL}...")
    print(f"Bidders: {num_bidders} | Iterations: {iterations}\n")

    for i in range(iterations):
        # 1. Generate new bids every iteration
        bids = generate_synthetic_bids(num_bidders)
        payload = {"bids": bids}
        
        # Start Clock
        start_time = time.perf_counter()
        
        # 2. Send data over network (to Azure/Nillion)
        response = requests.post(SERVER_URL, json=payload)
        
        # Stop Clock
        end_time = time.perf_counter()
        
        # 3. log time
        execution_time_ms = (end_time - start_time) * 1000
        times.append(execution_time_ms)
        
        if response.status_code != 200:
            print(f"Error during iteration {i}: {response.text}")

    # Save logs
    last_winner = response.json().get("winner")
    fastest_time = min(times)
    slowest_time = max(times)
    avg_time = mean(times)

    fastest_iter = times.index(fastest_time) + 1
    slowest_iter = times.index(slowest_time) + 1

    print("NETWORK RESUSLTS")
    print(f"Avrage time (RTT): {avg_time:.4f} ms")
    print(f"Fastest time: {fastest_time:.4f} ms, Iteration {fastest_iter})")
    print(f"Slowest time: {slowest_time:.4f} ms, Iteration {slowest_iter})")
    print(f"(Last winner was {last_winner['bidder_id']} with winning bid {last_winner['bid_amount']})")

if __name__ == "__main__":
    num_of_bidders = 100
    iterations_to_run = 100
    if len(sys.argv) > 1:
        num_of_bidders = int(sys.argv[1])
 
    if len(sys.argv) > 2:
        iterations_to_run = int(sys.argv[2])
        
    run_network_benchmark(num_bidders=num_of_bidders, iterations=iterations_to_run)