import time
import random
import os
import sys
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from main import dynamic_programming, reconstruction

ALPHABET = {'a': 2, 'b': 4, 'c': 5, 'd': 3, 'e': 7, 'f': 1}
TEST_LENGTHS = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250]


def generate_strings(length):
    chars = list(ALPHABET.keys())
    A = ''.join(random.choices(chars, k=length))
    B = ''.join(random.choices(chars, k=length))
    return A, B

def write_input(path, A, B):
    with open(path, 'w') as f:
        f.write(f"{len(ALPHABET)}\n")
        for ch, val in ALPHABET.items():
            f.write(f"{ch} {val}\n")
        f.write(f"{A}\n")
        f.write(f"{B}\n")

def write_output(path, max_val, subseq):
    with open(path, 'w') as f:
        f.write(f"{max_val}\n")
        f.write(f"{subseq}\n")

def run_benchmarks():
    random.seed(42)
    os.makedirs('data', exist_ok=True)
    runtimes = []
    print(f"{'Test':<6} {'Length':<8} {'Max Value':<12} {'Runtime (s)':<14}")

    for idx, length in enumerate(TEST_LENGTHS, start=1):
        A, B = generate_strings(length)

        in_path = os.path.join('data', f'test{idx:02d}.in')
        out_path = os.path.join('data', f'test{idx:02d}.out')
        write_input(in_path, A, B)

        start = time.perf_counter()
        dp = dynamic_programming(ALPHABET, A, B)
        answer = reconstruction(dp, ALPHABET, A, B)
        elapsed = time.perf_counter() - start

        max_val = dp[len(A)][len(B)]
        write_output(out_path, max_val, answer)
        runtimes.append(elapsed)

        print(f"{idx:<6} {length:<8} {max_val:<12} {elapsed:<14.6f}")

    return TEST_LENGTHS, runtimes

def plot_runtimes(lengths, runtimes):
    plt.figure(figsize=(10, 6))
    plt.plot(lengths, runtimes, 'bo-', linewidth=2, markersize=8)
    plt.xlabel('String Length (n)', fontsize=11)
    plt.ylabel('Runtime (seconds)', fontsize=11)
    plt.title('HVLCS Runtime vs. String Length', fontsize=15)
    plt.xticks(lengths)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    out_path = 'runtime_graph.png'
    plt.savefig(out_path, dpi=150)
    plt.show()
    print(f"\nRuntime graph saved to {out_path}")





if __name__ == '__main__':
    lengths, runtimes = run_benchmarks()
    plot_runtimes(lengths, runtimes)
