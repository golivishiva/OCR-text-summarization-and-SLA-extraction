📄 OCR + PDF Extraction + Text Summarization + SLA Extraction (Car Lease Contracts)

This project is built for an Infosys internship task focusing on document understanding, OCR, and contract information extraction.
It allows users to upload images or PDFs, extract text (even from scanned pages), generate a summary, and automatically extract key SLA fields like APR, monthly payment, mileage allowance, etc.
---------------------------------------
⭐ Features
🔍 1. OCR (Image / PDF Text Extraction)

Extracts text from images (.png, .jpg, .jpeg) using Tesseract OCR.

Extracts text from digital PDFs using PyPDF2.

Automatically detects scanned PDFs and uses:

pdf2image → converts pages to images

pytesseract → performs OCR on each page

Garbage text detection ensures clean and accurate extraction.
----------------------------------------
✂️ 2. Text Summarization (Groq API)

Uses Groq LLaMA-3.1 models to summarize long contract documents.

Converts lengthy legal content into clear, easy-to-understand summaries.
--------------------------------------
📌 3. SLA Field Extraction
--------------------------
Extracts structured information such as:

Interest Rate (APR)

Lease Term Duration

Monthly Payment

Down Payment

Residual Value

Mileage Limits & Overage Charges

Early Termination Clauses

Purchase Option Price

Maintenance Responsibilities

Warranty & Insurance Coverage

Penalties or Late Fees

All values are returned as JSON, ready to store or display.
