from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Bid(BaseModel):
    bidder_id: str
    bid_amount: int

class AuctionData(BaseModel):
    bids: list[Bid]

@app.post("/auction")
def run_blind_auction(data: AuctionData):
    
    winning_bid = max(data.bids, key=lambda x: x.bid_amount)
    
    return {
        "message": "Auction completed successfully",
        "winner": winning_bid
    }

@app.get("/")
def read_root():
    return {"message": "Auktions-servern är igång!"}