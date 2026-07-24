import random

# -------------------------------
# Naive String Matching Algorithm
# -------------------------------
def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)

    matches = []
    comparisons = 0

    for i in range(n - m + 1):
        j = 0
        while j < m:
            comparisons += 1
            if text[i + j] != pattern[j]:
                break
            j += 1

        if j == m:
            matches.append(i)

    return matches, comparisons


# -------------------------------
# Compute LPS Array for KMP
# -------------------------------
def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m

    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


# -------------------------------
# KMP Algorithm
# -------------------------------
def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)

    lps = compute_lps(pattern)

    matches = []
    comparisons = 0

    i = 0
    j = 0

    while i < n:
        comparisons += 1

        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            matches.append(i - j)
            j = lps[j - 1]

        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches, comparisons


# -------------------------------
# Rabin-Karp Algorithm
# -------------------------------
def rabin_karp(text, pattern, q=101):
    n = len(text)
    m = len(pattern)

    d = 256

    h = pow(d, m - 1, q)

    p_hash = 0
    t_hash = 0

    matches = []
    comparisons = 0

    # Initial hash values
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q

    # Slide the pattern
    for s in range(n - m + 1):

        if p_hash == t_hash:

            for k in range(m):
                comparisons += 1

                if text[s + k] != pattern[k]:
                    break
            else:
                matches.append(s)

        if s < n - m:
            t_hash = (
                d * (t_hash - ord(text[s]) * h)
                + ord(text[s + m])
            ) % q

            if t_hash < 0:
                t_hash += q

    return matches, comparisons


# ==========================================
# MAIN PROGRAM
# ==========================================
if __name__ == "__main__":

    print("=" * 60)
    print(" STRING MATCHING ALGORITHM COMPARISON")
    print("=" * 60)

    text = "AABAACAADAABAABA"
    pattern = "AABA"

    print("\nText    :", text)
    print("Pattern :", pattern)

    naive_matches, naive_comp = naive_search(text, pattern)
    kmp_matches, kmp_comp = kmp_search(text, pattern)
    rk_matches, rk_comp = rabin_karp(text, pattern)

    print("\nResults")
    print("-" * 60)
    print("Naive Algorithm")
    print("Matches      :", naive_matches)
    print("Comparisons  :", naive_comp)

    print("\nKMP Algorithm")
    print("Matches      :", kmp_matches)
    print("Comparisons  :", kmp_comp)

    print("\nRabin-Karp Algorithm")
    print("Matches      :", rk_matches)
    print("Comparisons  :", rk_comp)

    # --------------------------------------
    # Performance Comparison
    # --------------------------------------

    print("\n")
    print("=" * 60)
    print("Performance Comparison")
    print("=" * 60)

    text_large = "".join(random.choices("ABCD", k=10000))

    patterns = [
        "AB",
        "ABCD",
        "ABCDAB",
        "ABCDABCD",
    ]

    print(f'{"Pattern":>15}{"Naive":>15}{"KMP":>15}{"Rabin-Karp":>18}')
    print("-" * 65)

    for pat in patterns:
        _, n_comp = naive_search(text_large, pat)
        _, k_comp = kmp_search(text_large, pat)
        _, r_comp = rabin_karp(text_large, pat)

        print(f"{pat:>15}{n_comp:>15}{k_comp:>15}{r_comp:>18}")
