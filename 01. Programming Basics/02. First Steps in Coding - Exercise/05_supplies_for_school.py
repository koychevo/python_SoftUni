pens_package_price = 5.80
markers_package_price = 7.20
abstergent_price = 1.20

pens_packages_count = int(input())
markers_packages_count = int(input())
abstergent_count = int(input())
discount = int(input()) / 100

total_sum = (1 - discount) * (
        pens_packages_count * pens_package_price + markers_packages_count * markers_package_price + abstergent_count * abstergent_price)
print(total_sum)
