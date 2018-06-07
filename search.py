from bs4 import BeautifulSoup
import requests
search_results=[]
i=0
def main():
	global i
	query=input("Enter your query: ")

	if query=="another":#if first result does not make things clear and we want a better answer.
		i=i+1
		print (search_results[i])
	else:
		i=0
		keyword=query.replace(" ","+")
		google_search="https://www.google.co.in/search?sclient=psy-ab&client=ubuntu&hs=k5b&channel=fs&biw=1366&bih=648&noj=1&q="+keyword
		r=requests.get(google_search)#<Response [200]> means it was a success
		soup=BeautifulSoup(r.text,"html.parser")
		url=soup.findAll('span',{"class":"st"})
		for u in url:
			search_results.append(u.text)
		print(search_results[0])

if __name__=='__main__':
	while 1:#while we don't get an understandable result
		main()