import click
import whisper
import os
import logging
from tqdm import tqdm

SUPPORTED_FORMATS = (".wav", ".mp3", ".m4a", ".flac", ".aac")
SUPPORTED_LANGUAGES = {
    "ar": "Arabic", "zh": "Chinese", "da": "Danish", "nl": "Dutch",
    "en": "English", "fi": "Finnish", "fr": "French", "de": "German",
    "el": "Greek", "hi": "Hindi", "hu": "Hungarian", "it": "Italian",
    "ja": "Japanese", "ko": "Korean", "pl": "Polish", "pt": "Portuguese",
    "ru": "Russian", "es": "Spanish", "sv": "Swedish", "tr": "Turkish"
}


@click.command()
@click.argument('input_audio', type=click.Path(exists=True), required=True)
@click.option(
    '-l', '--language', default="en",
    help="Language for transcription. Options: " + ", ".join(
        f"{k} ({v})" for k, v in SUPPORTED_LANGUAGES.items()) + ". Default is 'en' for English."
)
@click.option('-m', '--model', 'model_name', default="small",
              help="Whisper model type (e.g., 'tiny', 'base', 'small', 'medium', 'large'). Default is 'small'.")
@click.option('-o', '--output-text', type=click.Path(),
              help="Path to save the transcribed text. Defaults to the same path as audio with .txt extension.")
@click.option('-v', '--verbose', is_flag=True, help="Enable detailed logging.")
@click.option('-L', '--log', type=click.Path(), help="Log file to save errors.")
def transcribe(input_audio, language, model_name, output_text, verbose, log):
    """Transcribes the provided audio file(s) using the Whisper model."""

    # Configure logger
    logging.basicConfig(filename=log, level=logging.DEBUG if verbose else logging.ERROR)
    logger = logging.getLogger(__name__)

    click.echo(f"Loading model '{model_name}'...")
    model = whisper.load_model(model_name)

    # Check if input is a single file or a directory
    if os.path.isfile(input_audio):
        files_to_process = [input_audio]
    else:
        files_to_process = [
            os.path.join(input_audio, f) for f in os.listdir(input_audio)
            if f.lower().endswith(SUPPORTED_FORMATS)
        ]

    # Overall progress bar
    with tqdm(total=len(files_to_process), desc="Processing files", unit="file") as pbar:
        for audio_path in files_to_process:
            try:
                # Define output path for each file
                output_file = output_text or f'{os.path.splitext(audio_path)[0]}-{model_name}.txt'

                # Transcribe audio without individual file progress
                result = model.transcribe(audio_path, language=language)

                # Save transcription
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(result["text"])

                pbar.update(1)

            except Exception as e:
                error_msg = f"Error processing '{audio_path}': {str(e)}"
                if verbose:
                    click.echo(error_msg)
                else:
                    click.echo(f"Error processing '{audio_path}'")

                logger.error(error_msg)
                pbar.update(1)

    click.echo("Processing complete!")


if __name__ == '__main__':
    transcribe()
