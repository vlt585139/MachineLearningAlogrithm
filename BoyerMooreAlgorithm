def buildtabell(orden):
    bad_char_table = {}
    for i in range(len(orden) - 1):
        bad_char_table[orden[i]] = len(orden) - 1 - i
    return bad_char_table

def boyermooresok(text, orden):
    m = len(orden)
    n = len(text)
    bad_char_table = buildtabell(orden)
    comparisons = 0
    matches = []

    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and orden[j] == text[i + j]:
            j -= 1
            comparisons += 1

        if j < 0:
            matches.append(i)
            i += m
        else:
            bad_char_shift = bad_char_table.get(text[i + j], m)
            i += max(1, bad_char_shift)
    
    return matches, comparisons

# Insert a phrase and orden
norsk_tekst = "Solen"
orden = "len"

matches, comparisons = boyermooresok(norsk_tekst, orden)
print("orden tree funnet i pos:", matches)
print("Total comp:", comparisons)

