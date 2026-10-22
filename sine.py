"""Example runPython target: computes sine and cosine waves. Stdlib only"""
import math


def main(n: int = 80, freq: float = 1.0) -> dict:
    print(f"computing {n} points at freq={freq}")
    sine = []
    cosine = []
    for i in range(n):
        x = i / (n - 1) if n > 1 else 0.0
        sine.append([x, math.sin(10 * math.pi * freq * x)])
        cosine.append([x, math.cos(10 * math.pi * freq * x)])
    return {"sine": sine, "cosine": cosine}
