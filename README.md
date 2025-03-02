# tartunlp_tts
# Tartu NLP TTS Custom Component for Home Assistant

This custom component integrates Tartu NLP's Text-to-Speech (TTS) service with Home Assistant, allowing users to convert text into spoken audio. The service specializes in Estonian language speech synthesis with multiple voice options.

## Description

The Tartu NLP TTS component for Home Assistant makes it possible to use the Tartu NLP API to generate spoken audio from text. This can be used in automations, assistants, scripts, or any other component that supports TTS within Home Assistant. *No API key is required for this service.*

## Features

- Text-to-Speech conversion using Tartu NLP's API
- Support for Estonian language
- Multiple Estonian voice options (mari, tambet, liisu, kalev, meelis, albert, külli, peeter, indrek, vesta, riina, eva, tõnu)
- Adjustable speech speed
- Integration with Home Assistant's assistant, automations and scripts

## Sample Home Assistant service

```
service: tts.speak
target:
  entity_id: tts.tartunlp_tts_mari
data:
  cache: true
  media_player_entity_id: media_player.bedroom_speaker
  message: Tere, kuidas läheb?
```

## HACS installation ( *preferred!* ) 

1. Go to the sidebar HACS menu 

2. Click on the 3-dot overflow menu in the upper right and select the "Custom Repositories" item.

3. Copy/paste https://github.com/yourusername/tartunlp_tts into the "Repository" textbox and select "Integration" for the category entry.

4. Click on "Add" to add the custom repository.

5. You can then click on the "Tartu NLP TTS Speech Services" repository entry and download it. Restart Home Assistant to apply the component.

6. Add the integration via UI and select your preferred speaker voice and speed. Multiple instances may be configured with different voices.

## Manual installation

1. Ensure you have a `custom_components` folder within your Home Assistant configuration directory.

2. Inside the `custom_components` folder, create a new folder named `tartunlp_tts`.

3. Place the repo files inside `tartunlp_tts` folder.

4. Restart Home Assistant

5. Add the integration via UI and select your preferred speaker voice and speed. Multiple instances may be configured.

## API Reference

This integration uses the Tartu NLP Text-to-Speech API v2:
- Endpoint: https://api.tartunlp.ai/text-to-speech/v2
- Documentation: [Tartu NLP API Documentation](https://api.tartunlp.ai/)

## Notes

- This service is optimized for Estonian language text
- No API key is currently required, but the integration supports adding one if needed in the future
- Speech speed can be adjusted between 0.5 (slower) and 2.0 (faster)