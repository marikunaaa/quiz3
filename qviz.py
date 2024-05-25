import requests
import json
import sqlite3

link = "https://api.kanye.rest/"

result = requests.get(link)

result2 = result.json()

print(f"status code: {result.status_code}\n"
      f"header: {result.headers['Date']}\n"
      f"Random kanye's quote: {result2['quote']}")


with open('info.json', "w") as file:
      json.dump(result2, file, indent=4)


conn = sqlite3.connect("info2.sqlite")
curr = conn.cursor()

curr.execute("""create table if not exists main
(id integer primary key autoincrement,
quote text)""")

curr.execute('''insert into main (quote) values (?)''',result2["quote"])

conn.commit()
conn.close()




