from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.imageanalysis.models import VisualFeatures

VISION_KEY="ANvorZGf596sYilctc406Qbs3g4GLKLS8NwLN9kyiOAUfFmQHpJZJQQJ99CEACYeBjFXJ3w3AAAFACOGNZl5"
VISION_ENDPOINT="https://projvision.cognitiveservices.azure.com/"

client = ImageAnalysisClient(
endpoint=VISION_ENDPOINT,
credential=
AzureKeyCredential(
VISION_KEY
)
)

def extract_text(image_bytes):
    result = client.analyze(
    image_data=image_bytes,
    visual_features=[
    VisualFeatures.READ
    ]
    )

    output = ""
    if result.read:
        for block in result.read.blocks:
            for line in block.lines:
                output += line.text + " "

    return output