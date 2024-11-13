# Transcriber

Transcriber is a CLI tool for audio transcription using OpenAI's Whisper model. It supports common audio formats and provides options for configuring the language and model used in the transcription.

## Features

- Supports transcription of common audio formats (`.wav`, `.mp3`, `.m4a`, `.flac`, `.aac`)
- CLI built with Click for easy command-line interaction
- Configurable transcription model and language settings

## Prerequisites

- Python 3.12
- [Pipenv](https://pipenv.pypa.io/en/latest/) for managing dependencies locally

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/alexandre-slp/transcriber.git
   cd transcriber
   ```

2. Install dependencies locally using Pipenv:

   ```bash
   pipenv install
   ```

3. Generate the `requirements.txt` file if needed for additional environments:

   ```bash
   pipenv requirements > requirements.txt
   ```

## Usage

To use the CLI, activate your Pipenv environment:

```bash
pipenv shell
python transcribe.py /path/to/audio/file.wav -o /path/to/output.txt -v
```

This command will process the audio file and output the transcription to a text file.

### CLI Options

- `-l`, `--language`: Specify the language of the audio (default is "en").
- `-m`, `--model`: Whisper model type (e.g., "tiny", "base", "small", "medium", "large").
- `-o`, `--output-text`: Path to save the transcribed text.
- `-v`, `--verbose`: Enable detailed logging.
- `-L`, `--log`: Path to a log file for error messages.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements.
