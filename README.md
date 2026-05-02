# File Integrity Checker 🔐

A Python-based cybersecurity project that verifies file integrity using SHA-256 hashing. This tool helps detect unauthorized file modifications by comparing file hash values before and after changes.

## Overview
File integrity is an important concept in cybersecurity. If a file is modified, corrupted, or tampered with, its cryptographic hash changes. This project uses the SHA-256 hashing algorithm to generate and compare file hashes for integrity verification.

## Features
✅ Generates SHA-256 hash of any file  
✅ Detects file modifications or tampering  
✅ Lightweight and beginner-friendly  
✅ Useful for cybersecurity learning and digital verification  

## Technologies Used
- Python 3
- hashlib library
- File handling

## How It Works
1. Select a file to monitor.
2. The program generates its SHA-256 hash.
3. Store the original hash.
4. Recheck the file later.
5. If the hash changes, the file has been modified.

## Project Structure

File_Integrity_Checker/
│── file_integrity_checker.py
│── README.md

## How to Run
### Step 1: Clone the repository
```bash
git clone <your-repository-url>
```
### Step 2: Open the project folder
```bash
cd File_Integrity_Checker
```
### Step 3: Run the Python file
```bash
python file_integrity_checker.py
```
*(Use `python3` if needed.)*
### Step 4: Enter the file path
Example:
```bash
sample.txt
```
The program will generate the file hash and check whether the file has been modified.

## Future Improvements
- GUI version
- Real-time file monitoring
- Email alerts
- Multiple hash algorithms

## Author
Anjali Kumari  
BTech CSE (IoT & Cybersecurity)  
Cybersecurity & Web Development Enthusiast
