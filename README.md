# Text Embeddings and Similarity Search

This project demonstrates the use of embeddings to perform semantic similarity search on text samples. It is a simple example that utilizes the `txtai` module for creating and searching embeddings. The project consists of several Python scripts that write text samples to files, generate embeddings for the text samples, perform interactive similarity search, and test various search queries.

## 1. Writing Text Samples to Files

The script `01_write_text_samples_to_file.py` defines a set of text samples and writes each sample to a separate text file. The filenames are chosen to reflect the content of each text sample. The text files are saved in the `text_samples` directory.

To execute the script, run:

```bash
python 01_write_text_samples_to_file.py
```

## 2. Generating Embeddings

The script `02_generate_embeddings.py` creates an instance of the `txtai` `Embeddings` class and specifies a pre-trained model for creating embeddings. It reads the content of the text files from the `text_samples` directory and generates embeddings for each text sample. The embeddings are indexed and saved to the `embeddings_index` directory for later use.

To execute the script, run:

```bash
python 02_generate_embeddings.py
```

## 3. Interactive Similarity Search

The script `03_interactive_search.py` provides an interactive interface for users to perform similarity searches on the indexed embeddings. Users can input search queries, and the script will return the most similar text samples based on the embeddings. It can also detect an "obvious winner" when one result is significantly more similar than the others.

To execute the script, run:

```bash
python 03_interactive_search.py
```

## 4. Testing Search Queries

The script `04_test_search_embeddings.py` tests various search queries by calling the `search_embeddings` function from the `search_embeddings.py` script. It demonstrates different types of search results, including cases where there is an "obvious winner" and cases where a cluster of similar results is returned.

To execute the script, run:

```bash
python 04_test_search_embeddings.py
```

## Conclusion

This project provides a simple example of how embeddings can be used to perform semantic similarity search on text samples. By utilizing the `txtai` module, users can create embeddings for text data, index them for efficient search, and perform interactive searches to find the most similar content. The project demonstrates the power of language models and embeddings for text-based applications.
