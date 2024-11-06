import sys
import os

# Check if the number of arguments is less than 2
if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

# Get the arguments
markdown_file = sys.argv[1]
output_file = sys.argv[2]

# Check if the Markdown file exists
if not os.path.exists(markdown_file):
    print(f"Missing {markdown_file}", file=sys.stderr)
    sys.exit(1)

# If all checks pass, proceed to convert Markdown to HTML
# For now, this part does nothing, you can add your conversion logic here

# Exit with no output (success)
sys.exit(0)
