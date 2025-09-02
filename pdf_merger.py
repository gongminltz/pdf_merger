import os
import argparse
from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(input_files, output_file):
    """
    Merge multiple PDF files into one PDF file.
    :param input_files: Paths of the PDF files to be merged.
    :param output_file: Output path of the PDF file.
    """
    pdf_writer = PdfWriter()
    for input_file in input_files:
        print(f"start merging file {input_file}")
        if not os.path.exists(input_file):
            print(f"file {input_file} does not exist，ignore")
            continue
        pdf_reader = PdfReader(input_file)
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)
        print(f"file {input_file} has been successfully merged, with a total of {len(pdf_reader.pages)} pages merged.")
    with open(output_file, "wb") as out:
        pdf_writer.write(out)
    print(f"The PDF file has been merged into {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Merge multiple PDF files into one PDF file.")
    parser.add_argument("input_files", nargs="+", help="Paths of the PDF files to be merged.")
    parser.add_argument("-o", "--output", required=True, help="Output path of the PDF file.")
    args = parser.parse_args()

    merge_pdfs(args.input_files, args.output)

if __name__ == "__main__":
    main()