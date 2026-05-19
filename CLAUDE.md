# Security Tools Portfolio

## Project Overview
Python-based cybersecurity tools for learning and portfolio demonstration.

## Coding Standards
- All scripts must include docstrings
- Use ANSI colors for terminal output (green=success, red=warning, yellow=info)
- Include educational comments explaining security concepts
- Handle errors gracefully with try/except
- Never hardcode credentials or API keys

## File Structure
- `portscanner.py` - TCP port scanner with threading
- `packet_sniffer.py` - Network packet analyzer with Scapy
- `log_analyzer.py` - Log file threat detection (next project)
- `README.md` - Project documentation

## Security Rules
- All scripts must print "For educational use only"
- Never suggest attacking systems without permission
- Include defensive countermeasures for every offensive technique shown

## Testing
- Test on localhost (127.0.0.1) only
- Use sudo only when necessary (packet sniffing)
- Document expected output in comments
