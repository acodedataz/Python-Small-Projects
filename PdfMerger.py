"""
📌 Project Name   : PDF Merger Tool Project__01
👨‍💻 Developer     : Rahatul Hossen Shanto
📅 Date           : 06-04-2026
📚 Course         : Python Foundation (80 Lectures Completed)

📖 Description:
This project merges multiple PDF files into a single PDF file.
It checks if each file exists before merging and handles errors gracefully.
"""

# ============================
# 📦 Import Required Modules
# ============================
from PyPDF2 import PdfMerger
import os


# ============================
# 📂 Function: Merge PDFs
# ============================
def merge_pdfs(pdf_list, output_name):
    """
    This function merges multiple PDF files.

    Parameters:
    pdf_list (list)   : List of PDF file names
    output_name (str) : Final merged PDF file name
    """

    merger = PdfMerger()

    try:
        # 🔁 Loop through all PDFs
        for pdf in pdf_list:
            if os.path.exists(pdf):
                print(f"📥 Adding: {pdf}")
                merger.append(pdf)
            else:
                print(f"❌ File not found: {pdf}")

        # 💾 Save merged PDF
        merger.write(output_name)

        print("\n✅ PDF Merge Completed Successfully!")
        print(f"📄 Output File: {output_name}")

    except Exception as e:
        print("\n❌ Error Occurred:", e)

    finally:
        merger.close()


# ============================
# 🚀 Main Program Start
# ============================
if __name__ == "__main__":
    # 📑 List of PDF files
    all_pdfs = ["lorem1.pdf", "lorem2.pdf", "lorem3.pdf"]

    # 📄 Output file name
    output_file = "Final_Merger.pdf"

    # 🔥 Call function
    merge_pdfs(all_pdfs, output_file)
