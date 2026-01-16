from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional
import json

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

# create a schema for how your data would be stored
class Review(TypedDict):
    key_themes : Annotated[list[str], "Mention the key themes discussed in the review in a list"]
    summary : Annotated[str,"a brief summary of the review"]
    sentiment : Annotated[str,"return sentiment of the review , positive, negative or neutral"]
    # Optional means, if we don't provide them, its not an issue
    pros : Annotated[Optional[list[str]],"mention the pros discussed in the review in a list"]
    cons : Annotated[Optional[list[str]],"mention the cons discussed in the review in a list"]
    
# call the with_structured_output function
structured_model = model.with_structured_output(schema=Review)


# now invoke the structured model
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

# with open(r"Structured_Output\TypedDict\review.json","w") as f:
#     json.dump(result,f)

print(result)