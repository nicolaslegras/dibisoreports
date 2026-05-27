import os
from os.path import join, split

from pypdf import PdfReader, PdfWriter
from pdfCropMargins import crop


def escape_for_latex(text: str) -> str:
    """
    Escapes all LaTeX special characters in a string.
    """
    latex_special_chars = {
        '#': r'\#',
        '$': r'\$',
        '%': r'\%',
        '&': r'\&',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\^{}',
        '\\': r'\textbackslash{}',
        '"': r'\textquotedbl{}',
        '<': r'\textless{}',
        '>': r'\textgreater{}',
    }
    escaped = []
    for char in text:
        if char in latex_special_chars:
            escaped.append(latex_special_chars[char])
        else:
            escaped.append(char)
    return ''.join(escaped)


def fix_plotly_pdf_export(pdf_file_path):
    pdf_reader = PdfReader(pdf_file_path)
    pdf_writer = PdfWriter()
    first_page = pdf_reader.pages[0]
    pdf_writer.add_page(first_page)
    with open(pdf_file_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)
    tmp_pdf_file_path = join(split(pdf_file_path)[0], "tmp-" + split(pdf_file_path)[1])
    crop(["-o", tmp_pdf_file_path, "-p", "0", pdf_file_path])
    os.remove(pdf_file_path)
    os.rename(tmp_pdf_file_path, pdf_file_path)