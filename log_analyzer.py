#!/usr/bin/env python3
"""
Security Log Analyzer

This script reads the /var/log/auth.log file to detect failed SSH login attempts
and identifies potential brute force attacks by counting failed attempts per IP address.
The script includes educational comments and uses ANSI color codes for visual alerts.
"""

import re
from collections import defaultdict

def analyze_auth_log(log_path='/var/log/auth.log'):
    """Analyze authentication log for failed SSH attempts and brute force attacks."""
    
    # Print the educational banner in yellow
    print("\033[93m╔══════════════════════════════════════════════════════════════╗\033[0m")
    print("\033[93m║           SECURITY LOG ANALYZER                              ║\033[0m")
    print("\033[93m║           For educational use only                           ║\033[0m")
    print("\033[93m╚══════════════════════════════════════════════════════════════╝\033[0m")
    print()
    
    # Attempt to read the authentication log file
    try:
        with open(log_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"\033[91mError: Log file not found: {log_path}\033[0m")
        print("\033[90mTip: Try running with sudo for system logs\033[0m")
        return
    except PermissionError:
        print(f"\033[91mError: Permission denied: {log_path}\033[0m")
        print("\033[90mTip: Run with sudo: sudo python3 log_analyzer.py\033[0m")
        return
    except Exception as e:
        print(f"\033[91mError reading log file: {e}\033[0m")
        return
    
    # Dictionary to track failed attempts per IP address
    failed_attempts = defaultdict(list)
    
    # Process each line in the log file
    for line in lines:
        # Look for failed SSH attempts
        if 'Failed password' in line or 'authentication failure' in line:
            # Extract timestamp and IP address
            match = re.search(
                r'(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}).*from\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',
                line
            )
            if match:
                timestamp = match.group(1)
                ip = match.group(2)
                failed_attempts[ip].append(timestamp)
    
    # Summary statistics
    total_failed = sum(len(timestamps) for timestamps in failed_attempts.values())
    unique_ips = len(failed_attempts)
    
    print(f"\033[96mAnalysis complete:\033[0m")
    print(f"  Total failed attempts: {total_failed}")
    print(f"  Unique source IPs: {unique_ips}")
    print()
    
    # Identify and report potential brute force attacks
    brute_force_threshold = 5
    threats_found = False
    
    for ip, timestamps in sorted(failed_attempts.items(), key=lambda x: len(x[1]), reverse=True):
        attempt_count = len(timestamps)
        
        if attempt_count >= brute_force_threshold:
            if not threats_found:
                print("\033[91m⚠️  POTENTIAL BRUTE FORCE ATTACKS DETECTED:\033[0m")
                threats_found = True
            
            print(f"\033[91m  [THREAT] {ip}: {attempt_count} failed attempts\033[0m")
            for ts in timestamps[:10]:  # Show first 10 timestamps
                print(f"    - {ts}")
            if len(timestamps) > 10:
                print(f"    ... and {len(timestamps) - 10} more")
            print()
        else:
            print(f"\033[90m  [INFO] {ip}: {attempt_count} failed attempt(s)\033[0m")
    
    if not threats_found:
        print("\033[92m✅ No brute force attacks detected (threshold: 5+ attempts)\033[0m")
    
    print()
    print("\033[93mFor educational use only. Always obtain proper authorization.\033[0m")

if __name__ == "__main__":
    analyze_auth_log()
