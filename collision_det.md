# Colission Detection
- You can detect collisisons after a frame has been received
- Depending on the medium you could during transmission as well

# CSMA with colission detection ( CSMA/CD )
- CSMA is a necessary but not sufficient for colission
- [Contention][Transmission][Contention][Transmission]
- Contention period: Decide who sends next
- Transmission period: Party (called station) who's been selected sens frame

## Contention slot
Contention period consists of slots
In each slot:
- stations start to send, if colission they stop
then
- wait random number of slots
- check if channel is free
- send again

## How much time to detect colission
- A starts sending at *t*
- B starts sending at *t+1*
- B detects colission & stops
- A only detects collision at *t+2*

# Collision-Free Protocols
(*very restrictive protocols*)

## Token ring
- Stations are arranged in a ring
- Pass `token` around the ring, station with token may send

## Bit-map protocol
- Hosts are static & known with common slots
1. Enumerate slots
2. Contention period: each station is assigned a slot to transmit the bit 1 if they have something to send 
3. Transmission period: all stations that indicated they have data, send one frame, in order of their station numbers

## Binary countdown
- Static and known stations that have distinct priorities
- Collision corresponds to bits sent at the same time
1. For N stations, assign priority 0 (lowest) to N-1
2. Express priority as binary numbers
3. Contention period: If wanting to send, station sends bit of priority starting with most significant bit
4. If 1 is received when 0 was sent station stop and waits for new round

eg. 

*Station priority* |<br>
`0010` -> 0 <br>
`0110` -> 0 <br>
`1010` -> 1 0  <br>
`1110` -> 1 1 <= gets to send next frame

