import os

# Define the text samples
sample_texts = [
    "The sunset was breathtaking. The vibrant hues of orange, red, and pink blended together, creating a stunning view. It was a magical evening by the beach.",
    "The library was filled with rows of books, each one containing a world of its own. The smell of old paper and ink filled the air, and the sound of turning pages echoed softly.",
    "The garden was a serene oasis, filled with colorful flowers and lush greenery. Butterflies fluttered from one blossom to another, while the gentle sound of water from the fountain added to the tranquility.",
    "The bustling market was alive with energy. Vendors called out to passersby, offering their wares. The aroma of freshly baked bread and exotic spices wafted through the air, enticing customers to explore.",
    "The concert was electrifying. The band's performance was incredible, and the crowd was swept up in the excitement. As the music resonated through the venue, fans sang along and danced with abandon."
]

# Define filenames that refer to the content of each text sample
filenames = [
    "Breathtaking_Sunset.txt",
    "Library_Books.txt",
    "Serene_Garden.txt",
    "Bustling_Market.txt",
    "Electrifying_Concert.txt"
]

# Output directory
output_dir = "text_samples"
os.makedirs(output_dir, exist_ok=True)

# Write each text sample to a separate file
for filename, text in zip(filenames, sample_texts):
    with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as file:
        file.write(text)

print("Text samples have been written to separate files in the 'text_samples' directory.")
