# Mini BitTorrent

A simple peer-to-peer file sharing system for the Computer Networks group project (Group 7).

A central tracker helps peers find each other. Peers split a file into fixed-size chunks, check every chunk with SHA-1, and download different chunks from several peers at the same time. Written in Python 3 with TCP sockets and threads. No outside packages are needed.

## Team and responsibilities

| Member | Roll No. | Owns | Responsibility |
|---|---|---|---|
| Ali Irtaza | 24P-0607 | `minitorrent/tracker.py` | Tracker server, peer registration, peer list protocol |
| Behzad Tariq | 24P-0616 | `minitorrent/peer.py` | Peer connections, chunk request and upload protocol, threading |
| Imdad Ali | 24P-0605 | `minitorrent/metadata.py` | Metadata file, chunking, hash checks, file reassembly |
| Ali Hussain | 24P-0618 | `minitorrent/cli.py` | Command-line interface, progress display, rarest-first selection |
| Waleed Ahmed | 24P-0637 | `tests/`, `report/` | Test setup, performance measurements, final report, demo |

`minitorrent/protocol.py` holds the message format that everyone shares. Agree on it as a team in weeks 1 to 2.

## Project layout

```
minitorrent/
  protocol.py   shared message format for tracker and peer messages
  tracker.py    tracker server
  peer.py       peer server and downloader
  metadata.py   metadata file, chunking, hashing, reassembly
  cli.py        command-line entry point
tests/          tests and performance scripts
report/         final report and performance results
docs/           project proposal
```

## How it works

1. A seeder makes a metadata file for a file and registers with the tracker.
2. A downloader reads the metadata file and asks the tracker for a list of peers.
3. The downloader connects to several peers and they swap lists of the chunks they have.
4. Missing chunks are requested from different peers in parallel, rarest first.
5. Each chunk is checked against its SHA-1 hash. Bad chunks are thrown away and requested again.
6. A checked chunk is announced and served to other peers.
7. When all chunks arrive, the file is put back together and saved.

## Running (planned commands)

```bash
python -m minitorrent.tracker --port 6000
python -m minitorrent.cli share path/to/file --tracker 127.0.0.1:6000
python -m minitorrent.cli download file.meta --out downloads/
```

## Timeline

| Week | Milestone |
|---|---|
| 1 to 2 | Message protocol design, tracker, metadata format |
| 3 to 4 | File chunking, hashing, single-peer transfer |
| 5 to 6 | Multi-peer parallel downloading |
| 7 | Interface, error handling, extra features |
| 8 | Testing, performance measurement, report, demo |
