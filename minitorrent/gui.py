"""Simple Tkinter window that demonstrates the full project.

Owner: Ali Irtaza
- One window runs the whole system: start the tracker, start several peers,
  share a file, and download it.
- Show a progress bar, connected peers, and which chunk came from which peer.
- Only calls functions from peer.py, metadata.py and tracker.py (no networking here).
- Update widgets from the main thread only (use root.after), since Tkinter is not thread-safe.
"""
