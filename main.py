import PyPDF2
import os


def split_pdf(file_path, output_folder, max_size_mb):
    input_pdf = PyPDF2.PdfReader(file_path)
    total_pages = len(input_pdf.pages)

    # Determine the number of parts to split into based on the file size
    file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
    num_parts = int(file_size_mb / max_size_mb) + 1

    pages_per_part = total_pages // num_parts
    for i in range(num_parts):
        output = PyPDF2.PdfWriter()
        start_page = i * pages_per_part
        end_page = (i + 1) * pages_per_part if i < num_parts - 1 else total_pages

        for j in range(start_page, end_page):
            output.add_page(input_pdf.pages[j])

        with open(f"{output_folder}/part_{i + 1}.pdf", "wb") as output_stream:
            output.write(output_stream)


# Example usage
split_pdf("./MedicineMCQ.pdf", "./Med", 100)
