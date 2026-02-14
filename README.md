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
# Then present you with an interactive menu with 22 options
```

### Usage Examples

#### Search username across all social networks
```
manuleye → [1] Username Hunt → enter username
```

#### Extract GPS coordinates from photo
```
manuleye → [11] EXIF Extract → select image
```

#### Analyze IP address
```
manuleye → [4] IP Geolocate → enter IP
```

#### Port scanning
```
manuleye → [16] Port Scanner → enter IP/domain
```

#### Create OSINT report
```
manuleye → [21] Create Paste → fill in information
```

## 📋 Requirements

- Python 3.8 or higher
- Internet connection (for online lookups)
- Operating System: Windows, Linux, macOS

### Dependencies

All dependencies are automatically installed:
- requests - HTTP requests
- rich - Beautiful terminal output
- pyfiglet - ASCII art banners
- Pillow - Image processing
- phonenumbers - Phone number analysis
- pypdf - PDF processing
- mutagen - Audio/video metadata
- python-docx - DOCX processing
- openpyxl - XLSX processing
- instaloader - Instagram OSINT
- maigret - Username search
- holehe - Email lookup

## ⚠️ Legal Disclaimer

This tool is intended for **legal and ethical use only**. Users are responsible for complying with all applicable laws and regulations. The developers assume no liability for misuse or damage caused by this program.

**Permitted use cases:**
- Security research and penetration testing (with permission)
- Digital forensics and investigations
- OSINT gathering for legitimate purposes
- Educational purposes
- Testing your own digital security

**DO NOT use for:**
- Unauthorized access to systems or data
- Harassment or stalking
- Violating others' privacy
- Any illegal activities

## 🎯 Main Functions

### LOOKUP Category
1. **Username Hunt** - Search across 500+ social networks
2. **Email Lookup** - Check email on various services
3. **Phone Intel** - Detailed phone number information
4. **IP Geolocate** - IP geolocation and information
5. **Domain Resolve** - Domain resolution and data collection

### EXPLOIT Category
6. **SQLMap** - Automated SQL injection testing
7. **XSStrike** - XSS vulnerability scanning
8. **Instagram OSINT** - Gather data from Instagram profiles

### METADATA Category
9. **Archive Info** - Analyze archive contents
10. **Meta Cleaner** - Remove metadata from images
11. **EXIF Extract** - Extract EXIF and GPS from photos
12. **PDF Metadata** - PDF document metadata
13. **Video Metadata** - Video file metadata
14. **Audio Metadata** - Audio file metadata
15. **Office Metadata** - Office document metadata

### NETWORK Category
16. **Port Scanner** - Port scanning
17. **Traceroute** - Route tracing
18. **Ping Sweep** - Find active hosts
19. **SSL Cert Info** - SSL certificate information
20. **HTTP Headers** - HTTP header analysis

### UTILITIES Category
21. **Create Paste** - Create structured OSINT report
22. **Password Gen** - Strong password generator

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### How to contribute:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- **GitHub:** https://github.com/b3stp4st3r/manuleye
- **Issues:** https://github.com/b3stp4st3r/manuleye/issues
- **PyPI:** https://pypi.org/project/manuleye/

## 👤 Author

**Daniil Pentium**
- GitHub: [@b3stp4st3r](https://github.com/b3stp4st3r)

## 🙏 Acknowledgments

- **Maigret** - Excellent username search tool
- **Holehe** - Email lookup tool
- All other open-source libraries used in this project

## 📊 Statistics

- 30+ OSINT functions
- 500+ supported platforms for username search
- 11 main dependencies
- Support for 3 operating systems
- 1100+ lines of code

## 🔥 Popular Use Cases

### 1. Complete identity investigation
```
1. Username Hunt - find all accounts
2. Email Lookup - check email
3. Phone Intel - analyze number
4. Create Paste - generate report
```

### 2. Web resource analysis
```
1. Domain Resolve - get IP
2. Port Scanner - find open ports
3. SSL Cert Info - check certificate
4. HTTP Headers - analyze headers
```

### 3. File metadata analysis
```
1. EXIF Extract - GPS from photos
2. PDF Metadata - information from PDF
3. Office Metadata - data from documents
```

## 💡 Usage Tips

- **Use VPN** for anonymity when gathering information
- **Always get permission** before testing systems
- **Save results** for investigation documentation
- **Combine tools** for complete picture
- **Verify information** from multiple sources

## 🆘 Support

If you encounter problems:
1. Check [Issues](https://github.com/b3stp4st3r/manuleye/issues)
2. Create a new Issue with problem description
3. Specify Python version and OS

## 🔄 Updates

Stay updated:
```bash
pip install --upgrade manuleye
```

Check current version:
```bash
pip show manuleye
```

## 🌟 Features

- ✅ Easy installation via pip
- ✅ Interactive menu
- ✅ Colorful terminal output
- ✅ Automatic dependency installation
- ✅ Cross-platform (Windows/Linux/macOS)
- ✅ Open source (MIT License)
- ✅ Active development and support
- ✅ Regular updates

## 📱 Contact

For questions and suggestions:
- Create an Issue on GitHub
- Contact the author via GitHub

---

**Stay sharp. Stay hidden.** 🦅

*Version: 1.0.1*  
*Last updated: February 15, 2026*

---

## ⭐ Support the Project

If you like the project, give it a star on GitHub!

[![GitHub stars](https://img.shields.io/github/stars/b3stp4st3r/manuleye?style=social)](https://github.com/b3stp4st3r/manuleye)
[![PyPI version](https://badge.fury.io/py/manuleye.svg)](https://pypi.org/project/manuleye/)
[![Python versions](https://img.shields.io/pypi/pyversions/manuleye.svg)](https://pypi.org/project/manuleye/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
