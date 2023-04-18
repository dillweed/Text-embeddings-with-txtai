from txtai.embeddings import Embeddings

def search_embeddings(query, threshold=0.1):
    # Load the pre-processed embeddings index from the 'embeddings_index' directory
    embeddings = Embeddings()
    embeddings.load("embeddings_index")

    # Perform a similarity search on the loaded embeddings
    results = embeddings.search(query, 5)

    # Analyze the search results
    if results:
        cluster, winner = get_top_scoring_cluster(results, threshold)

        if winner:
            print("An obvious winner was detected:")
        else:
            print("Top scoring cluster of results:")
        
        for result in cluster:
            print(f"  - File ID: {result[0]}, Similarity Score: {result[1]:.4f}")
    else:
        print("No matching results were found.")

def get_top_scoring_cluster(results, threshold):
    if len(results) >= 2 and (results[0][1] - results[1][1]) > threshold:
        return [results[0]], True

    cluster = []
    for i, result in enumerate(results):
        if i == 0 or abs(results[i-1][1] - result[1]) <= threshold:
            cluster.append(result)
        else:
            break

    return cluster, False
