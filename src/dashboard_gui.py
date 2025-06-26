# dashboard_gui.py
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from src.mapping_engine import map_journal_entries

def launch_dashboard():
    def run_simulation():
        try:
            oracle_df = pd.read_csv(entry_oracle.get())
            sap_df = pd.read_csv(entry_sap.get())
            results = map_journal_entries(oracle_df, sap_df)
            output_text.delete("1.0", tk.END)
            for o, s, score in results:
                output_text.insert(tk.END, f"Match Score: {score:.2f}\nOracle: {o}\nSAP: {s}\n---\n")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    root = tk.Tk()
    root.title("EduLedgerBridge Simulator")

    tk.Label(root, text="Oracle CSV:").grid(row=0, column=0)
    entry_oracle = tk.Entry(root, width=50)
    entry_oracle.grid(row=0, column=1)
    tk.Button(root, text="Browse", command=lambda: entry_oracle.insert(0, filedialog.askopenfilename())).grid(row=0, column=2)

    tk.Label(root, text="SAP CSV:").grid(row=1, column=0)
    entry_sap = tk.Entry(root, width=50)
    entry_sap.grid(row=1, column=1)
    tk.Button(root, text="Browse", command=lambda: entry_sap.insert(0, filedialog.askopenfilename())).grid(row=1, column=2)

    tk.Button(root, text="Run Simulation", command=run_simulation).grid(row=2, column=1, pady=10)

    output_text = tk.Text(root, height=20, width=80)
    output_text.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    root.mainloop()
