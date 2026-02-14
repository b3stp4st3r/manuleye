# MANUL-EYE 🦅

**Comprehensive OSINT Framework for Intelligence Gathering**

**English** | [Русский](README_RU.md)

MANUL-EYE is a powerful Open Source Intelligence (OSINT) framework designed for security researchers, penetration testers, and investigators. It provides a wide range of tools for gathering intelligence from various sources, extracting metadata, and performing network reconnaissance.

## ✨ Features

### 🔍 Lookup & Intelligence
- **Username Hunt** - Search for usernames across 500+ social media platforms (via Maigret)
- **Email Lookup** - Check email presence on various services (via Holehe)
- **Phone Intelligence** - Extract carrier, location, timezone info from phone numbers
- **IP Geolocation** - Get detailed information about IP addresses
- **Domain Resolution** - Resolve domains to IPs and gather information

### 🎯 Metadata Extraction
- **EXIF Extractor** - Extract GPS coordinates and metadata from images
- **PDF Metadata** - Extract author, creation date, and other PDF metadata
- **Video Metadata** - Analyze video file metadata
- **Audio Metadata** - Extract ID3 tags and audio file information
- **Office Documents** - Extract metadata from DOCX and XLSX files
- **Archive Info** - List contents of ZIP and TAR archives
- **Metadata Cleaner** - Remove EXIF data from images

### 🌐 Network Tools
- **Port Scanner** - Scan for open ports on target systems
- **Traceroute** - Trace network path to destination
- **Ping Sweep** - Discover alive hosts on a network
- **SSL Certificate Info** - Analyze SSL/TLS certificates
- **HTTP Headers Analyzer** - Check security headers and server information

### 🛡️ Security Tools
- **SQLMap Integration** - SQL injection testing
- **XSStrike Integration** - XSS vulnerability scanning
- **Instagram OSINT** - Gather public information from Instagram profiles

### 📝 Utilities
- **Create Paste** - Generate detailed OSINT reports
- **Password Generator** - Create strong, customizable passwords

## 📦 Installation

### From PyPI (Recommended)

```bash
pip install manuleye
```

### From Source

```bash
git clone https://github.com/b3stp4st3r/manuleye.git
cd manuleye
pip install -e .
```

## 🚀 Usage

Simply run the command in your terminal:

```bash
manuleye
```

The interactive menu will guide you through all available options.

### Quick Examples

```bash
# Launch the framework
manuleye

# The tool will automatically check and install missing dependencies
# Then present you with an interactive menu
```

## 📋 Requirements

- Python 3.8 or higher
- Internet connection (for online lookups)
- Operating System: Windows, Linux, macOS

### Dependencies

All dependencies are automatically installed:
- requests
- rich
- pyfiglet
- Pillow
- phonenumbers
- pypdf
- mutagen
- python-docx
- openpyxl
- instaloader
- maigret
- holehe

## ⚠️ Legal Disclaimer

This tool is intended for **legal and ethical use only**. Users are responsible for complying with all applicable laws and regulations. The developers assume no liability for misuse or damage caused by this program.

**Use cases:**
- Security research and penetration testing (with permission)
- Digital forensics and investigations
- OSINT gathering for legitimate purposes
- Educational purposes

**DO NOT use for:**
- Unauthorized access to systems or data
- Harassment or stalking
- Any illegal activities

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔗 Links

- GitHub: https://github.com/b3stp4st3r/manuleye
- Issues: https://github.com/b3stp4st3r/manuleye/issues
- PyPI: https://pypi.org/project/manuleye/

## 👤 Author

**Danya Pentium**
- GitHub: [@b3stp4st3r](https://github.com/b3stp4st3r)

## 🙏 Acknowledgments

- Maigret - Username search tool
- Holehe - Email lookup tool
- All other open-source libraries used in this project

---

**Stay sharp. Stay hidden.** 🦅