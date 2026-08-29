import logfire


def parse_text(file_path: str) -> str:
    """
    Parses plain text files.
    """
    with logfire.span("Text Parsing", filename=file_path):
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Add validation and success logs to align with your other loaders
            if not content.strip():
                logfire.warning(f"Text file is empty: {file_path}")
            else:
                logfire.info(f"Successfully read {len(content)} characters from text file.")

            return content
            
        except Exception as e:
            logfire.error(f"Text Parse Failed: {e}")
            raise e