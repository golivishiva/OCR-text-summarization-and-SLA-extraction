from ocr import OCR
from summarization import summarize_with_groq

# Change this to "sample.pdf" to test PDFs
FILE_PATH = "kgf.png"  # or "sample.pdf"

# Step 1: Extract text
ocr = OCR()
text = ocr.extract(FILE_PATH)

print("Extracted Text:\n")
print(text)
print("\n" + "-" * 40 + "\n")

# Step 2: Summarize the extracted text
summary = summarize_with_groq(text)

print("Summary:\n")
print(summary)
