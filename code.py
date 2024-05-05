import tkinter as tk
import webbrowser

def search_manga(category):
    url = f"https://lekmanga.net/manga/?category={category}"
    webbrowser.open(url)

def create_gui():
    window = tk.Tk()
    window.title("Manga Recommendation")
    
    categories = ["Action", "Drama", "Romance", "Adventure"]
    
    label = tk.Label(window, text="Choose a category:")
    label.pack()
    
    for category in categories:
        button = tk.Button(window, text=category, command=lambda cat=category: search_manga(cat))
        button.pack()
    
    window.mainloop()

if __name__ == "__main__":
    create_gui()