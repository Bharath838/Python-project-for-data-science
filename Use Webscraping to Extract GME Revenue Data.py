url1 = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
html_data = requests.get(url1).text
soup = BeautifulSoup(html_data, "html.parser")
soup.find_all('title')
gme_revenue = pd.DataFrame(columns=['Date', 'Revenue'])

for table in soup.find_all('table'):

    if ('GameStop Quarterly Revenue' in table.find('th').text):
        rows = table.find_all('tr')
        
        for row in rows:
            col = row.find_all('td')
            
            if col != []:
                date = col[0].text
                revenue = col[1].text.replace(',','').replace('$','')

                gme_revenue = gme_revenue.append({"Date":date, "Revenue":revenue}, ignore_index=True)

gme_revenue.tail()
