def get_num_words(text):
    print("----------- Word Count ----------")
    print(f"Found {len(text.split())} total words")

def count_chars(text):
    counts = {}
    for c in text:
        if c==" ":
            continue
        lower = c.lower()
        if lower in counts:
            counts[lower]["num"] += 1
        else:
            counts[lower] = {"char": lower, "num":1}
    return list(counts.values())

def sort_on(item):
    return item["num"]

def print_counts(counts):
    print("--------- Character Count -------")
    counts.sort(reverse=True, key=sort_on)
    for c in counts:
        print(f"{c['char']}: {c['num']}")
