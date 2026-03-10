
"""
Currency Converter using Fixer.io API
======================================
Converts currencies using live exchange rates from Fixer.io.

Usage:
    python currency_converter.py

Setup:
    1. Get a free API key at https://fixer.io/
    2. Set your API key in config.py or as an environment variable FIXER_API_KEY
"""

import os
import sys
import requests
from datetime import datetime



# Your Fixer API key — set via environment variable or paste it here directly.
# Get a free key at: https://fixer.io/
FIXER_API_KEY = os.getenv("FIXER_API_KEY", "d494f4ecf3e0e8d282e4000635a4060a")
FIXER_BASE_URL = "http://data.fixer.io/api"  # Free plan uses HTTP only



def get_latest_rates(base_currency: str = "EUR") -> dict:
    """
    Fetch the latest exchange rates from Fixer.io.

    Note: Free Fixer plan only supports EUR as base currency.
    For other base currencies, upgrade to a paid plan or we convert manually.
    """
    url = f"{FIXER_BASE_URL}/latest"
    params = {
        "access_key": FIXER_API_KEY,
        "base": base_currency,
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        if not data.get("success", False):
            error = data.get("error", {})
            raise ValueError(
                f"Fixer API Error [{error.get('code')}]: {error.get('info')}"
            )

        return data

    except requests.exceptions.ConnectionError:
        print("\n❌ No internet connection. Please check your network.")
        sys.exit(1)
    except requests.exceptions.Timeout:
        print("\n❌ Request timed out. Fixer API might be slow. Try again.")
        sys.exit(1)
    except requests.exceptions.HTTPError as e:
        print(f"\n❌ HTTP Error: {e}")
        sys.exit(1)


def convert_currency(
    amount: float, from_currency: str, to_currency: str, rates: dict
) -> float:
    """
    Convert an amount from one currency to another using fetched rates.

    Since Fixer free plan fixes base to EUR, we:
      1. Convert from_currency → EUR
      2. Convert EUR → to_currency
    """
    rates_map = rates.get("rates", {})

    if from_currency not in rates_map:
        raise ValueError(f"Currency '{from_currency}' not found in rates.")
    if to_currency not in rates_map:
        raise ValueError(f"Currency '{to_currency}' not found in rates.")

    # Convert to EUR base, then to target
    amount_in_eur = amount / rates_map[from_currency]
    result = amount_in_eur * rates_map[to_currency]
    return result


def get_supported_currencies(rates: dict) -> list:
    """Return a sorted list of all supported currency codes."""
    return sorted(rates.get("rates", {}).keys())


# ─────────────────────────── Display Helpers ──────────────────────────────────

def print_banner():
    banner = """
╔══════════════════════════════════════════════════╗
║          💱  LIVE CURRENCY CONVERTER              ║
║              Powered by Fixer.io                 ║
╚══════════════════════════════════════════════════╝
"""
    print(banner)


def print_supported_currencies(currencies: list):
    """Print all supported currencies in a nice grid."""
    print("\n📋 Supported Currencies:\n")
    cols = 8
    for i, code in enumerate(currencies):
        print(f"  {code:<6}", end="")
        if (i + 1) % cols == 0:
            print()
    print("\n")


# ─────────────────────────── Validation ───────────────────────────────────────

def validate_api_key():
    if FIXER_API_KEY == "YOUR_API_KEY_HERE" or not FIXER_API_KEY.strip():
        print(
            "\n⚠️  No API key detected!\n"
            "   Please set your Fixer API key:\n"
            "   • Option 1 (recommended): export FIXER_API_KEY='your_key_here'\n"
            "   • Option 2: Edit 'currency_converter.py' and replace "
            "'YOUR_API_KEY_HERE' with your key.\n"
            "   Get a free key at: https://fixer.io/\n"
        )
        sys.exit(1)


def get_valid_currency(prompt: str, supported: list) -> str:
    """Prompt user until they enter a valid currency code."""
    while True:
        code = input(prompt).strip().upper()
        if code in supported:
            return code
        print(f"   ❌ '{code}' is not supported. Type 'list' to see all currencies.")
        if code == "LIST":
            print(", ".join(supported))


def get_valid_amount(prompt: str) -> float:
    """Prompt user until they enter a valid positive number."""
    while True:
        raw = input(prompt).strip()
        try:
            amount = float(raw)
            if amount <= 0:
                print("   ❌ Amount must be greater than zero.")
                continue
            return amount
        except ValueError:
            print(f"   ❌ '{raw}' is not a valid number.")


# ─────────────────────────── Main App ─────────────────────────────────────────

def run_converter():
    """Main interactive loop for the currency converter."""
    print_banner()
    validate_api_key()

    print("⏳ Fetching live exchange rates from Fixer.io...")
    rates_data = get_latest_rates(base_currency="EUR")

    timestamp = rates_data.get("timestamp", 0)
    date_str = datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M UTC")
    supported = get_supported_currencies(rates_data)

    print(f"✅ Rates loaded! Last updated: {date_str}")
    print(f"   Total currencies available: {len(supported)}")

    while True:
        print("\n" + "─" * 52)
        print("  Options:  [C] Convert   [L] List currencies   [Q] Quit")
        print("─" * 52)
        choice = input("  Enter choice: ").strip().upper()

        if choice == "Q":
            print("\n👋 Goodbye! Happy currency converting!\n")
            break

        elif choice == "L":
            print_supported_currencies(supported)

        elif choice == "C":
            print()
            from_currency = get_valid_currency(
                "  From currency (e.g. USD): ", supported
            )
            to_currency = get_valid_currency(
                "  To currency   (e.g. INR): ", supported
            )
            amount = get_valid_amount(
                f"  Amount in {from_currency}: "
            )

            try:
                result = convert_currency(amount, from_currency, to_currency, rates_data)
                rate = convert_currency(1, from_currency, to_currency, rates_data)

                print(f"""
  ┌─────────────────────────────────────────────┐
  │  {amount:>14,.4f}  {from_currency}                           │
  │            =                                │
  │  {result:>14,.4f}  {to_currency}                           │
  │                                             │
  │  Rate: 1 {from_currency} = {rate:.6f} {to_currency:<10}       │
  │  Source: Fixer.io ({date_str})   │
  └─────────────────────────────────────────────┘""")

            except ValueError as e:
                print(f"\n  ❌ Conversion error: {e}")

        else:
            print("  ❌ Invalid option. Please enter C, L, or Q.")




if __name__ == "__main__":
    run_converter()
