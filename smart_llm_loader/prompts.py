DEFAULT_CHUNK_PROMPT = """OCR the following page into Markdown format. 
- All tables, charts, and other visual elements must be formatted in Markdown.
- Do not exclude any content from the page.
- Chunk the page into sections with same semantic theme.
- Our goal is to identify parts of the page with same semantic theme. These chunks will
be embedded and used in a RAG pipeline.
- All chunks must be in Markdown format.

Images in the document should be properly described in details such that an LLM can understand the
image and answer questions about the image without seeing the image.
The image description should be returned as a chunk too.
"""

DEFAULT_PAGE_CHUNK_PROMPT = """OCR the following page into Markdown format. 
- All tables must be formatted in Markdown.
- The contents of the page should be returned as a single chunk.
- Do not exclude any content from the page.
- Also return the semantic theme of the page.

Images in the document should be properly described in details such that an LLM can understand the image and answer
questions about the image without seeing the image.
The description should be returned as a part of the page content.
"""