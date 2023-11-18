import requests
from bs4 import BeautifulSoup
import lxml
import openpyxl

url = "https://allo.ua/ua/products/internet-planshety/"
user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
headers = {"User-agent": user}

session = requests.Session()

response = session.get(url, headers=headers)

book = openpyxl.Workbook()
book.save("catalog.xlsx")
sheet = book.active
sheet["A1"] = "Title"
sheet["B1"] = "Review"
sheet["C1"] = "Price"
count = 2

for j in range(1, 26):
    print(f'Page {j}')
    with open('catalog.txt', "a", encoding="utf-8") as file:
        url = f'https://allo.ua/ua/products/internet-planshety/p-{j}/'
        response = session.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "lxml")
            all_products = soup.find_all("div", class_="products-layout__item")
            for i in all_products:
                if i.find('a', class_="product-card__title"):
                #if i.find('div', class_="product-card__content"):

                    if i.find('a', class_="product-card__title"):
                        title = i.find('a', class_="product-card__title")
                        print(title.text)
                    else:
                        # try:
                        #     title = i.find('a', class_="product-card__title")
                        # except AttributeError:
                        print("Немає назви")
                    # print(title.text)
                    if i.find('a', class_="review-button__text review-button__text--count"):
                        title = i.find('span', class_="review-button__text review-button__text--count")
                        print(title.text)
                    else:
                        try:
                            title = i.find('span', class_="review-button__text review-button__text--count")
                        except AttributeError:
                            print("Немає назви")
                        # title = i.find('a', class_="product-card__title")
                        # print(title.text)
                        # try:
                        #     review = i.find('span', class_="review-button__text review-button__text--count").text
                        # except AttributeError:
                        #     print("Немає відгуків")
                        # print(review)
                        if i.find('div', class_="v-pb__cur"):
                            price = i.find('div', class_="v-pb__cur")
                            print(price.text)
                        else:
                            print("Немає ціни")

                else:
                    print("Error")
                # file.write(f"{title.text}{review.text}{price.text} \n")


        for i in range(len(all_products)):

                title = all_products[i].find('a', class_="product-card__title")
                try:
                    review = all_products[i].find('span', class_="review-button__text review-button__text--count").text
                except AttributeError:
                    print('Немає відгуків')
                price = all_products[i].find('div', class_="v-pb__cur")
                try:
                    file.write(f"{title.text} {review} {price.text} \n")
                except AttributeError:
                    print("Помилка")
                try:
                    sheet[f"A{count}"] = title.text
                except AttributeError:
                    print("Немає назви")

                sheet[f"B{count}"] = review

                try:
                    sheet[f"C{count}"] = price.text
                except AttributeError:
                    print("Немає ціни")

                count = + 1


book.save('catalog.xlsx')
book.close()

book = openpyxl.Workbook()
book.save("catalog2.xlsx")
sheet = book.active
sheet["A1"] = "Title"
sheet["B1"] = "Review"
sheet["C1"] = "Price with sale"
count = 2

for j in range(1, 26):
     print(f'Page {j}')
     with open('catalog.txt', "a", encoding="utf-8") as file:
         url = f'https://allo.ua/ua/products/internet-planshety/p-{j}/'
         response = session.get(url, headers=headers)

         if response.status_code == 200:
             soup = BeautifulSoup(response.text, "lxml")
             all_products = soup.find_all("div", class_="products-layout__item")
             for i in all_products:
                 if i.find('div', class_="v-pb__old"):
                 #if i.find('div', class_="product-card__content"):

                         if i.find('a', class_="product-card__title"):
                             title = i.find('a', class_="product-card__title")
                             print(title.text)
                         else:
                             try:
                                 title = i.find('a', class_="product-card__title")
                             except AttributeError:
                                 print("Немає назви")
                         #print(title.text)
                         if i.find('a', class_="review-button__text review-button__text--count"):
                             title = i.find('span', class_="review-button__text review-button__text--count")
                             print(title.text)
                         else:
                             try:
                                 title = i.find('span', class_="review-button__text review-button__text--count")
                             except AttributeError:
                                 print("Немає відгуків")
                         # try:
                         #     review = i.find('span', class_="review-button__text review-button__text--count").text
                         # except AttributeError:
                         #     print("Немає відгуків")
                         # print(review)
                         if i.find('div', class_="v-pb__cur discount"):
                              price_with_sale = i.find('div', class_="v-pb__cur discount")
                              print(price_with_sale.text)

                 else:
                     print("Error")
                 # file.write(f"{title.text}{review.text}{price.text} \n")


         for i in range(len(all_products)):

                 title = all_products[i].find('a', class_="product-card__title")
                 try:
                     review = all_products[i].find('span', class_="review-button__text review-button__text--count").text
                 except AttributeError:
                     print('Немає відгуків')
                 price = all_products[i].find('div', class_="v-pb__cur")
                 try:
                     file.write(f"{title.text} {review} {price.text} \n")
                 except AttributeError:
                     print("Error")
                 try:
                     sheet[f"A{count}"] = title.text
                 except AttributeError:
                     print("Немає назви")

                 sheet[f"B{count}"] = review

                 #try:
                 sheet[f"C{count}"] = price_with_sale.text
                 #except AttributeError:
                     #print("Немає ціни")

                 count = + 1

book.save('catalog2.xlsx')
book.close()