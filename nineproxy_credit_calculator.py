#!/usr/bin/env python3
"""
9Proxy Pay-per-IP Residential Proxy Credit & Volume Discount Calculator 2026.
Calculates effective rate per IP and volume savings without expiration.
"""
import argparse

def calculate_credits(ips, tier_rate, promo_discount):
    gross_cost = ips * tier_rate
    discount_amount = gross_cost * (promo_discount / 100.0)
    net_total = gross_cost - discount_amount
    effective_rate = net_total / ips if ips > 0 else 0.0
    return {
        "ips": ips,
        "tier_rate": tier_rate,
        "promo_discount": promo_discount,
        "gross_cost": gross_cost,
        "discount_amount": discount_amount,
        "net_total": net_total,
        "effective_rate": effective_rate
    }

def main():
    parser = argparse.ArgumentParser(description="9Proxy Residential Credit Calculator")
    parser.add_argument("--ips", type=int, default=500, help="Number of residential proxy IPs (default: 500)")
    parser.add_argument("--tier-rate", type=float, default=0.30, help="Tier rate per IP in USD (default: $0.30)")
    parser.add_argument("--promo-discount", type=float, default=10.0, help="Promotional code discount in percent (default: 10.0%)")
    args = parser.parse_args()

    res = calculate_credits(args.ips, args.tier_rate, args.promo_discount)
    print(f"IP Package Quantity:     {res['ips']} IPs")
    print(f"Standard Catalog Rate:   ${res['tier_rate']:.2f}/IP")
    print(f"Gross Purchase Cost:     ${res['gross_cost']:.2f}")
    print(f"Promotional Savings:     ${res['discount_amount']:.2f}")
    print(f"Net Purchase Total:      ${res['net_total']:.2f}")
    print(f"Effective Rate Per IP:   ${res['effective_rate']:.4f}/IP")

if __name__ == "__main__":
    main()
