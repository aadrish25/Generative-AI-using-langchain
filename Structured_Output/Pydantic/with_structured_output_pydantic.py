from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import Optional
from pydantic import BaseModel,Field

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

# create schema of the data using pydantic
class Review(BaseModel):
    
    key_themes : list[str] = Field(description="Write down all the key themes from the review")
    summary : str = Field(description="Generate a brief summary of the review")
    sentiment : str = Field(description="Sentiment of the review, either positive,negative or neutral")
    
    # optional fields
    pros : Optional[list[str]] = Field(description="Write down all the pros from the review",default=None)
    cons : Optional[list[str]] = Field(description="Write down all the cons from the review",default=None)
    # reviewer_name : Optional[str] = Field(description="Write the name of the person who has written the review",default=None)
    
# create the structured model
structured_model = model.with_structured_output(schema=Review)

result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don’t use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful

Cons:
Bulky and heavy—not great for one-handed use
Bloatware still exists in One UI
Expensive compared to competitors""")

print(result)
    
     