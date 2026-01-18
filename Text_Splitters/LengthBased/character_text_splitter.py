from langchain_text_splitters import CharacterTextSplitter



text = """Space exploration has led to incredible scientific discoveries. From landing on the Moon to exploring Mars, humanity continues to push the boundaries of what’s possible beyond our planet.

These missions have not only expanded our knowledge of the universe but have also contributed to advancements in technology here on Earth. Satellite communications, GPS, and even certain medical imaging techniques trace their roots back to innovations driven by space programs."""

# create an instance
splitter = CharacterTextSplitter(
    chunk_size = 100, # 100 characters per chunk
    chunk_overlap=0, # no characters of previous chunk is repeated in the next chunk
    separator=''
)

# apply splitter on text
result = splitter.split_text(text) # the chunks are returned in a list

print(result)