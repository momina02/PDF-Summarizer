# PDF Summarization Tool

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Model%20Integration-blueviolet)

## Project Description

This **PDF Summarization Tool** extracts text from uploaded PDF files and generates concise summaries using state-of-the-art Natural Language Processing (NLP) models. By leveraging models from **Hugging Face** or other text generation models, the tool processes the content of PDFs and summarizes them into easily digestible insights. 

The tool uses **Hugging Face API**, **PyPDF** for PDF parsing, and **Langchain** to organize and run NLP models effectively.

## Features

- **Extract text** from PDF documents
- **Summarize** the key points in 3-6 sentences
- Supports large PDFs by splitting text into manageable chunks
- Integration with Hugging Face and OpenAI models for summarization
- **Easy to use**: Just upload your PDF, and the tool will generate the summary

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/pdf-summarization-tool.git
cd pdf-summarization-tool
```

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:

```bash
streamlit run app.py
```

2. Upload a PDF file via the interface.
3. The tool will extract the text, process it, and generate a summary.

## Example

Upload a PDF document like a research paper or article, and the tool will return a concise 3-5 sentence summary of its content.

## Contributing

Feel free to fork the project and create pull requests! Contributions are always welcome.

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Hugging Face](https://huggingface.co/) for providing state-of-the-art models.
- [PyPDF](https://pypi.org/project/pypdf/) for PDF text extraction.
- [Streamlit](https://streamlit.io/) for an easy-to-use interface.
