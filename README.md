# Multbank Automation

A powerful automation tool for multbank operations using UV and Selenium Base.

## Description

Multbank Automation is a Python-based automation tool designed to streamline banking operations through automated web interactions. Built with Selenium Base, this tool provides a reliable framework for performing repetitive banking tasks efficiently.

## Prerequisites

Before installing Multbank Automation, ensure you have the following installed:

- **Python 3.12+**: This project requires Python version 3.12 or higher
- **UV**: A fast Python package installer and resolver. Install UV by following the [official installation guide](https://github.com/astral-sh/uv?tab=readme-ov-file#installation)
- **Web Browser**: Google Chrome or Firefox (for Selenium WebDriver)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/inovvia/multbank-automation.git
   cd multbank-automation
   ```

2. Install dependencies using UV:
   ```bash
   uv sync
   ```

   This command will:
   - Create a virtual environment in the `.venv` directory
   - Install all project dependencies from `pyproject.toml`
   - Download and install the exact versions specified in `uv.lock`

## Usage

To run the automation tool:

```bash
uv run python main.py
```

## Configuration

### Browser Drivers

Selenium Base requires browser drivers to work properly. The tool will attempt to download the appropriate drivers automatically, but you can also install them manually:

- **Chrome**: Download ChromeDriver from [Google's official site](https://sites.google.com/a/chromium.org/chromedriver/)
- **Firefox**: Download GeckoDriver from [Mozilla's official site](https://github.com/mozilla/geckodriver/releases)

Make sure the driver executables are in your system's PATH.

### Environment Variables

You may want to configure the following environment variables (optional):

- `BROWSER`: Set to `chrome`, `firefox`, or other supported browsers (default: Chrome)
- `HEADLESS`: Set to `true` to run in headless mode (default: false)

## Assumptions

- **Screen Resolution**: We assume that traders would have a minimum of 1080p screen (1920x1080). The automation framework validates the UI based on this resolution to ensure all elements are properly displayed and interactive.

## Project Structure

```
multbank-automation/
├── .venv/                 # Virtual environment (auto-generated)
├── .gitignore             # Git ignore file
├── .python-version        # Python version specification
├── README.md              # This file
├── main.py                # Main entry point of the application
├── pyproject.toml         # Project configuration and dependencies
└── uv.lock                # Dependency lock file
```

## Development

To contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests (if available)
5. Submit a pull request

## Dependencies

- **seleniumbase>=4.44.20**: A powerful framework for building reliable, maintainable Selenium tests and automated web scripts

## Troubleshooting

### Issues with UV

If you encounter problems with UV:

1. Make sure UV is installed correctly:
   ```bash
   uv --version
   ```

2. Clear UV cache:
   ```bash
   uv cache clean
   ```

3. Re-sync dependencies:
   ```bash
   uv sync --refresh
   ```

### Issues with Selenium Base

1. Update browser drivers:
   ```bash
   uv run python -c "from seleniumbase import Driver; Driver().quit()"
   ```

2. Verify browser installation:
   ```bash
   google-chrome --version  # For Chrome
   firefox --version        # For Firefox
   ```
