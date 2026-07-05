# Gym Check‑In Logging System
This system checks whether a member’s ID is active and logs their visit to a text file.
It combines dictionary lookups, file handling, and exception management.

## Features
- Active members stored in a dictionary
- Function check_in_member() handles ID validation
- Writes each successful check‑in to visitors_log.txt
- Handles invalid input (ValueError)
- Handles disk errors (IOError)
- Runs until the user types "stop"

# How to use
Enter your membership ID.
Valid ID → access granted and saved to the log file.
Unknown ID → access denied.
Invalid input → error message.
Type "stop" to exit.


## Learning Purpose
Practice with:
- dictionaries as a simple database
- file handling (open, write mode)
- exception handling
- separating logic into modules and packages
- building a small real‑world style check‑in system
