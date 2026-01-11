count = 0

try:
    with open("story.txt", encoding="utf-8") as f:
        for row in f:
            row = row.strip()
            if row:
                count += len(row.split())

    print(f"Liczba słów: {count}")
except FileNotFoundError:
    print("Plik story.txt nie istnieje.")
