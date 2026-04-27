from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 1. Definiera hur ett enskilt bud ser ut (din dictionary)
class Bid(BaseModel):
    bidder_id: str
    bid_amount: int

# 2. Definiera att vi förväntar oss en lista med sådana bud
class AuctionData(BaseModel):
    bids: list[Bid]

@app.post("/auction")
def run_blind_auction(data: AuctionData):
    
    # 3. Exakt samma logik som i din baseline! 
    # Vi hittar det bud som har högst 'bid_amount'
    winning_bid = max(data.bids, key=lambda x: x.bid_amount)
    
    # 4. Returnera hela vinnar-objektet (Både ID och Summa)
    return {
        "message": "Auction completed successfully",
        "winner": winning_bid
    }

@app.get("/")
def read_root():
    return {"message": "Auktions-servern är igång!"}