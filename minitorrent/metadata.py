"""Metadata file, chunking, hashing and reassembly.

Owner: Imdad Ali
- Metadata holds: file name, size, chunk size, number of chunks,
  SHA-1 of every chunk, tracker address.
- Split a file into fixed-size chunks and check each chunk against its hash.
- Put the chunks back together into the final file.
"""
