# Ethernet

## Minimum frame size
Maximum time it takes for a signal to travel between 2 stations sharing the medium: Δ
- Collision detection can take 2Δ

 Very small frames: Sender is done sending before receiving colission signal
- Sender unsure whether collision affected frame, thus we need a minimum size for frames

**The longer the frame the more efficient Ethernet is**

**When detecting a collision stations warns others by a 48-bit noise burst**

## CSMA/CD in Ethernet
Uses 1-p CSMA/CD, with a random backoff using a Binary Exponential Backoff (BEP) (chose randomly from set { 0, 1, ..., 2^i - 1 } where i is the # of failed tries)
