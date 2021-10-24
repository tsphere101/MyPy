import webbrowser as wb

search_word = input("Enter search word: ")
url_search = 'https://www.google.co.th/search?q=' + search_word
wb.open(url_search)