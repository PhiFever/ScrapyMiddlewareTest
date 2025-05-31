## Description

This project demonstrates the issue discussed in Scrapy [issue #6843](https://github.com/scrapy/scrapy/issues/6843) through a minimal reproducible example.

## Setup and Usage

### Prerequisites
Install `uv` following the official guide: [Installation | uv](https://docs.astral.sh/uv/getting-started/installation/)

### Running the Project

1. **Install dependencies:**
   ```bash
   uv sync

2. **Run the test application:**

   ```bash
   uv run app.py
   ```

3. **Execute the Scrapy spider:**

   ```bash
   uv run scrapy crawl ScrapyMiddlewareTest
   ```

   