from fastapi import FastAPI
from pydantic import BaseModel
import openai
from schema import AdInput
# from dotenv import load_dotenv
import os

# Initialize FastAPI app
app = FastAPI()




# load_dotenv()

openai.api_type     = "azure"
openai.api_base     = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_version  = "2023-09-15-preview"
openai.api_key      = os.getenv("AZURE_OPENAI_API_KEY")



# Route to generate ad
@app.post("/generate_ad/")
async def generate_ad(input_data: AdInput):
    language_for=input_data.language,
    writing_for=input_data.writing_for,
    website_or_landingPageURl=input_data.website_or_landingPageURl

    # Define prompt
    prompt = f"""
    You are a skilled content creator selling software based on the data we get tasked with generating Google Ads twitter ads bing ads facebook ads linkedin ads for {language_for}. 
    The target audience is {writing_for}. The key features and benefits are {website_or_landingPageURl}.

    Please create 1 set for each social media platform mentioned above, set containing:
    - their website on top
    - 1 description (up to 90 characters) with a picture
    - it should be like posting into social media

    The copy should be attention-grabbing, highlight the unique selling points, and persuade the audience to click on the ad. Please format the output as follows:

    Headline 1:
    their url:
    Description:
    Call-to-Action:
    """

    # Generate ad from OpenAI
    response = openai.Completion.create(
    engine="anycopychatgpt35",
    prompt=prompt,
    temperature=1,
    max_tokens=350,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None)

    # Extract ad text from OpenAI response
    ad_text = response.choices[0].text.strip()

    return {"generated_ad": ad_text}

