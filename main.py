import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog
from tkinter import ttk
from ttkthemes import ThemedTk
import scraper
import pandas as pd

class WebScraperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Scraper App")
        self.root.geometry("800x600")
        self.root.minsize(600, 400)
        self.root.maxsize(1200, 800)

        self.style = ttk.Style(self.root)
        self.style.theme_use("arc")

        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        ttk.Label(self.frame, text="URL:").grid(row=0, column=0, padx=10)
        self.url_entry = ttk.Entry(self.frame, width=50)
        self.url_entry.grid(row=0, column=1, padx=10)

        scrape_btn = ttk.Button(self.frame, text="Scrape", command=self.scrape_data)
        scrape_btn.grid(row=0, column=2, padx=10)

        output_label = ttk.Label(self.frame, text="Output Type:")
        output_label.grid(row=1, column=0, padx=10, pady=10)

        self.output_type = tk.StringVar(value="Headers")
        headers_rbtn = ttk.Radiobutton(self.frame, text="Headers", variable=self.output_type, value="Headers")
        headers_rbtn.grid(row=1, column=1, padx=10, pady=10)
        links_rbtn = ttk.Radiobutton(self.frame, text="Links", variable=self.output_type, value="Links")
        links_rbtn.grid(row=1, column=2, padx=10, pady=10)

        export_btn = ttk.Button(self.frame, text="Export to CSV", command=self.export_to_csv)
        export_btn.grid(row=2, column=1, pady=10)

        self.output_text = scrolledtext.ScrolledText(self.root, width=80, height=20, wrap=tk.WORD)
        self.output_text.grid(row=1, column=0, padx=10, pady=10)

        self.scraped_data = []

    def scrape_data(self):
        url = self.url_entry.get()
        output_type = self.output_type.get()
        if url:
            try:
                self.scraped_data = scraper.scrape(url, output_type)
                self.output_text.delete(1.0, tk.END)
                for item in self.scraped_data:
                    self.output_text.insert(tk.END, item + "\n")
                messagebox.showinfo("Success", "Scraping completed successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to scrape the website: {e}")
        else:
            messagebox.showwarning("Warning", "Please enter a URL.")

    def export_to_csv(self):
        if self.scraped_data:
            file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
            if file_path:
                try:
                    df = pd.DataFrame(self.scraped_data, columns=[self.output_type.get()])
                    df.to_csv(file_path, index=False)
                    messagebox.showinfo("Success", "Data exported to CSV successfully.")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to export data: {e}")
        else:
            messagebox.showwarning("Warning", "No data to export.")

if __name__ == "__main__":
    root = ThemedTk(theme="arc")
    app = WebScraperApp(root)
    root.mainloop()
