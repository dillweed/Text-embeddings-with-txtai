import os
from txtai.embeddings import Embeddings

# Create an instance of the Embeddings class with the specified model
embeddings = Embeddings({"path": "sentence-transformers/all-MiniLM-L6-v2"})

# Folder containing text files
folder = "text_samples"

# Initialize a list to store data for indexing
data_to_index = []

# Iterate through the text files in the folder
for file_name in os.listdir(folder):
    # Check if the file has a .txt extension
    if file_name.endswith(".txt"):
        # Create the full file path
        file_path = os.path.join(folder, file_name)
        # Read the file content
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # Store the file name as the identifier and the content for indexing
            data_to_index.append((file_name, content, None))

# Index the data to create embeddings
embeddings.index(data_to_index)

# Save the embeddings index to a file for later use
embeddings.save("embeddings_index")

# Load the embeddings index from the file when needed for search comparison
loaded_embeddings = Embeddings()
loaded_embeddings.load("embeddings_index")

# Perform a similarity search on the loaded embeddings
result = loaded_embeddings.search("search query", 3)
print(result)
