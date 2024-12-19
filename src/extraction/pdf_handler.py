from parsestudio.parse import PDFParser
import requests
import tempfile
import os
from typing import Optional
import logging

class DocumentHandler:
    def __init__(self):
        self.parser = PDFParser(parser="docling")
        
    def get_document_content(self, url: str) -> Optional[str]:
        try:
            response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, stream=True, timeout=30)
            response.raise_for_status()
            
            if 'application/pdf' not in response.headers.get('content-type', '').lower():
                return None

            with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as temp_pdf:
                temp_pdf.write(response.content)
                temp_path = temp_pdf.name

            try:
                outputs = self.parser.run(temp_path, modalities=["text", "tables"])
                return outputs[0].text if outputs else None
            finally:
                os.unlink(temp_path)

        except Exception as e:
            logging.error(f"Failed to process PDF: {str(e)}")
            return None