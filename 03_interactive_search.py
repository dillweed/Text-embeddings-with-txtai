from txtai.embeddings import Embeddings

# Load the pre-processed embeddings index from the 'embeddings_index' directory
embeddings = Embeddings()
embeddings.load("embeddings_index")

# Print usage instructions
print("Welcome to the text search application!")
print("You can search for text that is similar to the provided text samples.")
print("To exit the application, type 'exit' and press Enter.")

def get_top_scoring_cluster(results, threshold=0.1):
    # Check if there's an obvious winner
    if len(results) >= 2 and (results[0][1] - results[1][1]) > threshold:
        return [results[0]], True

    # Get a cluster of top scoring results with close similarity scores
    cluster = []
    for i, result in enumerate(results):
        if i == 0 or abs(results[i-1][1] - result[1]) <= threshold:
            cluster.append(result)
        else:
            break

    return cluster, False

while True:
    # Prompt the user for input text
    query = input("Enter your search query: ")

    # Exit the application if the user types 'exit'
    if query.lower() == 'exit':
        print("Thank you for using the text search application. Goodbye!")
        break

    # Perform a similarity search on the loaded embeddings
    results = embeddings.search(query, 5)

    # Analyze the search results
    if results:
        cluster, winner = get_top_scoring_cluster(results)

        if winner:
            print("An obvious winner was detected:")
        else:
            print("Top scoring cluster of results:")
        
        for result in cluster:
            print(f"  - File ID: {result[0]}, Similarity Score: {result[1]:.4f}")
    else:
        print("No matching results were found.")

    # Ask the user if they want to perform another search
    continue_search = input("Would you like to perform another search? (yes/no): ")
    if continue_search.lower() != 'yes':
        print("Thank you for using the text search application. Goodbye!")
        break
