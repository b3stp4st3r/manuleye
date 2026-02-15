"""
MANUL-EYE OSINT Framework
~~~~~~~~~~~~~~~~~~~~~~~~~

A comprehensive OSINT (Open Source Intelligence) framework for intelligence gathering,
metadata extraction, network reconnaissance, and security analysis.

Features:
- Username and email lookup across multiple platforms
- Phone number intelligence gathering
- IP geolocation and domain resolution
- EXIF and metadata extraction from images, PDFs, videos, audio, and documents
- Network scanning (ports, SSL certificates, HTTP headers)
- Security testing tools integration
- Paste creation for OSINT reports
- Password generation

Usage:
    $ manuleye

:copyright: (c) 2026 by MANUL-EYE Team
:license: MIT, see LICENSE for more details.
"""

__version__ = "1.1.0"
__author__ = "MANUL-EYE Team"
__license__ = "MIT"

from manuleye.main import main

__all__ = ["main"]
