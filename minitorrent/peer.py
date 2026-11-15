"""Peer: acts as both client and server.

Owner: Behzad Tariq
- Listen for other peers and serve chunks we already have (one thread per connection).
- Connect to peers, swap chunk lists, request chunks in parallel.
- Announce newly verified chunks.
"""
