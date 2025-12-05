import streamlit as st
from ocr import OCR
from summarization import summarize_with_groq
from contract_extraction import extract_sla_with_groq   # 👈 NEW
from PIL import Image
import tempfile
import os

# Create OCR object once
ocr = OCR()

st.set_page_config(page_title="OCR + PDF + SLA Extraction", layout="centered")

st.title("📄 Car Contract OCR + SLA Extraction + Summary")
st.write(
    "Upload an **image** or **PDF** of a car lease/loan contract.\n\n"
    "The app will:\n"
    "1. Extract text (OCR / PDF).\n"
    "2. Summarize the contract.\n"
    "3. Extract key SLA fields like APR, term, payments, penalties, etc."
)

uploaded_file = st.file_uploader(
    "Upload an image or PDF file",
    type=["png", "jpg", "jpeg", "pdf"]
)

if uploaded_file is not None:
    file_name = uploaded_file.name
    ext = os.path.splitext(file_name)[1].lower()

    # Image preview
    if ext in [".png", ".jpg", ".jpeg"]:
        image = Image.open(uploaded_file)
        st.image(image, caption=f"Uploaded Image: {file_name}", use_column_width=True)
    else:
        st.info(f"📑 PDF uploaded: **{file_name}**")

    if st.button("Extract Text, Summarize & Extract SLA"):
        # Save uploaded file to temp
        with st.spinner("Saving uploaded file..."):
            suffix = ext if ext else ".tmp"
            with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
                tmp.write(uploaded_file.read())
                temp_path = tmp.name

        # 1️⃣ Extract text
        with st.spinner("Extracting text (OCR / PDF)..."):
            extracted_text = ocr.extract(temp_path)

        st.subheader("📜 Extracted Text")
        st.text_area("OCR / PDF Output", extracted_text, height=250)

        if isinstance(extracted_text, str) and extracted_text.strip():

            # 2️⃣ Summary
            with st.spinner("Summarizing with Groq..."):
                summary = summarize_with_groq(extracted_text)

            st.subheader("✂ Summary")
            st.text_area("Summary Output", summary, height=200)

            # 3️⃣ SLA Extraction
            with st.spinner("Extracting SLA fields with Groq..."):
                sla_data = extract_sla_with_groq(extracted_text)

            st.subheader("📌 Extracted Contract SLA Fields")

            if "error" in sla_data:
                st.error(sla_data["error"])
                if "raw" in sla_data:
                    with st.expander("Raw model output"):
                        st.write(sla_data["raw"])
            else:
                st.json(sla_data)

        else:
            st.warning(
                "No text detected. If this is a scanned PDF, make sure the text is readable."
            )
else:
    st.info("Please upload a contract PDF/image to start.")
