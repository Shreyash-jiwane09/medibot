import streamlit as st

def pdf_uploader():
    """Create a file uploader for PDF documents"""
    return st.file_uploader(
        'Upload PDF files', 
        type='pdf', 
        accept_multiple_files=True,
        help="Upload one or more medical PDF documents"
    ) 