# EthernetDetector
Python script for detecting ethernet frames in binary files.

### Why?
I was wondering how often you could find random, valid ethernet frames in binary "files", e.g. `/dev/urandom`.

### Are aliens communicating secretly through `/dev/urandom`?
No, at least not regularly. I couldn't detect a single valid ethernet frame.

### How long would I have to wait to detect a random ethernet frame?
A long time I would guess. `/dev/urandom` would have to guess 64 bit correctly in order to generate a valid preamble.
On average that would require 2^63 = 9,223,372,036,854,775,807 guesses.
My computer can generate 1,512,064,068 random bits per second.

Assuming (for simplicity) I would always take 64 bits at once and not read them as stream, my computer could make 1,512,064,068 / 64 = 23,626,001 guesses per second.
That would result in an average wait time of:
  * 390,390,740,983 seconds
  * or 6,506,512,349 minutes
  * or 108,441,872 hours
  * or 4,518,411 days
  * or **12,379** years
  
As a result, if you do happen to find a valid ethernet frame in `/dev/urandom`, then you are either very lucky or just observed someone communicating through randomness.