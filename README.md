# Web Scraper for Exam Questions

## Overview
This script extracts questions from a specified webpage (`https://myschool.ng/classroom/english-language`). It parses the page content, collects question details, retrieves their correct answers, and saves the data in a JSON file (`data.json`) for future use.

## Features
- Fetches questions, options, and question numbers from the webpage.
- Retrieves the correct answer for each question by following the answer link.
- Outputs the scraped data in a structured JSON format.
- Handles multiple pages by adjusting the `page_number` parameter.
- Supports retries for failed requests.

## Requirements
- Python 3.x
- Required Python libraries:
  - `lxml`
  - `requests`
  - `os`
  - `json`

## Installation
1. Install Python 3.x from the official [Python website](https://www.python.org/).
2. Install required libraries:
   ```bash
   pip install lxml requests
   ```

## Usage
1. Place the script in a directory of your choice.
2. Create a subdirectory named `data.json` in the same directory where the script will save the output.
3. Run the script:
   ```bash
   python script_name.py
   ```
   Replace `script_name.py` with the name of the script file.

## How It Works
1. **Fetch Data**: The script sends a GET request to the specified URL with the required headers.
2. **Parse HTML**: It uses `lxml` to parse the HTML content and extract questions, options, and links to answers.
3. **Retrieve Answers**: For each question, the script follows the answer link to retrieve the correct answer.
4. **Save Data**: The results are saved in `data.json` in a structured format.

## JSON Format
The output file `data.json` contains an array of question objects:
```json
[
    {
        "qst": "Question text",
        "opt": "Option A\nOption B\nOption C\nOption D",
        "ans": ["Correct Answer: Option A"]
    },
    ...
]
```

## Customization
- **Change Page Number**: Update the `page_number` variable to fetch questions from a different page.
- **Modify Headers**: Adjust the headers in the `headers` dictionary if needed.

## Error Handling
- The script attempts to handle connection errors and logs failures to retrieve answers.
- If an answer cannot be retrieved, the question will still be included in the output without an answer.

## Notes
- Ensure the target URL structure remains unchanged, as changes might break the script.
- Use this script ethically and respect the terms of service of the target website.

## License
This project is open-source and available for modification and redistribution under the MIT License.
