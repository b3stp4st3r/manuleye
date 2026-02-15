"""Social media OSINT modules."""

from .telegram import telegram_search
from .tiktok import tiktok_search
from .vk import vk_search

__all__ = ['telegram_search', 'tiktok_search', 'vk_search']
