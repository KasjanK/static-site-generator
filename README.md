# Static Website Generator

This project is a static site generator built to transform Markdown files into a complete, navigable HTML website.

## What it does

This tool takes a directory of Markdown files, processes them, and outputs a corresponding directory of HTML files, along with any necessary assets like CSS. It automates the process of converting simple text content into a fully formed website, ready for deployment.

## How it works

The generator typically works by:
1. **Reading Markdown files:** It scans a specified input directory for all `.md` files.
2. **Parsing Markdown:** Each Markdown file is parsed into HTML content.
3. **Applying a template:** The generated HTML content is then inserted into a pre-defined HTML template (e.g., `base.html` or similar) to ensure consistent styling and navigation across all pages.
4. **Copying assets:** Any static assets like CSS, images, or JavaScript files are copied to the output directory.
5. **Outputting HTML:** The final HTML files are written to a specified output directory, maintaining a similar directory structure to the input.

## Features

*   **Markdown to HTML Conversion:** Easily convert `.md` files into valid HTML.
*   **Template Integration:** Apply a consistent look and feel using a customizable HTML template.
*   **Static Asset Copying:** Automatically include CSS, images, and other resources.
*   **Directory Structure Preservation:** Maintain an organized output matching your input source.
*   **Customizable:** Easily extendable to add new features or change themes.
