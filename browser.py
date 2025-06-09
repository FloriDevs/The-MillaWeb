import tkinter as tk
import requests
import webbrowser

def fetch_url():
    url = entry.get()
    response = requests.get(url)
    text.delete(1.0, tk.END)
    html_content = response.text
    text.insert(tk.END, html_content)
    
    # Links extrahieren und anzeigen
    display_links(html_content)

def display_links(html_content):
    text_links.delete(1.0, tk.END)  # Vorherige Links löschen

    # Hier können wir die Links aus dem HTML-Inhalt extrahieren
    for line in html_content.splitlines():
        if line.startswith("Link:"):
            link = line.split("Link: ")[1].strip()
            text_links.insert(tk.END, link + '\n')

def open_link(event):
    selected_link = text_links.get(tk.SEL_FIRST, tk.SEL_LAST)
    webbrowser.open(selected_link)

root = tk.Tk()
root.title("Simple Browser")

entry = tk.Entry(root, width=50)
entry.pack()

button = tk.Button(root, text="Fetch", command=fetch_url)
button.pack()

text = tk.Text(root, wrap=tk.WORD, height=15)
text.pack()

text_links = tk.Text(root, wrap=tk.WORD, height=5)
text_links.pack()

# Link-Textfeld klickbar machen
text_links.bind("<Button-1>", open_link)

root.mainloop()
