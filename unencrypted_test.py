import time
import random
from statistics import mean

def generate_synthetic_bids(num_bidders):
    """Generates a list of dictionaries containing random bids."""
    bids = []
    for i in range(num_bidders):
        bids.append({
            "bidder_id": f"Party_{i+1}",
            "bid_amount": random.randint(100, 10000)
        })
    return bids

def run_local_auction(bids):
    """Finds the bidder with the highest bid."""
    winner = max(bids, key=lambda x: x["bid_amount"])
    return winner


# MEASUREMENT AND EXECUTION
if __name__ == "__main__":
    num_bidders = 100
    iterations = 100 
    
    times = []

    print(f"Starting benchmark for {num_bidders} parties over {iterations} iterations...")

    for i in range(iterations):
        # 1. Generate new test data for this iteration
        bids = generate_synthetic_bids(num_bidders)
    
        # 2. Start the timer
        start_time = time.perf_counter()
    
        # 3. Execute the auction logic
        winning_bid = run_local_auction(bids)
    
        # 4. Stop the timer
        end_time = time.perf_counter()
    
        # 5. Calculate and store the execution time
        execution_time_ms = (end_time - start_time) * 1000
        times.append(execution_time_ms)
    
    # Calculate the average time
    avg_time = mean(times)

    # Print the results once at the end
    print("\n=== BENCHMARK RESULTS (BASELINE) ===")
    print(f"Number of bidders: {num_bidders}")
    print(f"Number of iterations: {iterations}")
    print(f"Average execution time: {avg_time:.6f} ms")
    print(f"(Example from the last iteration - Winner: {winning_bid['bidder_id']} with {winning_bid['bid_amount']})")