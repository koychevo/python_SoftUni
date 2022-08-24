easter_bread_count = int(input())
packages_eggs_count = int(input())
cookies_count = int(input())

costs =easter_bread_count * 3.20 + packages_eggs_count * 4.35 + packages_eggs_count * 12 * 0.15 + cookies_count * 5.40
print(f"{costs:.2f}")