import search_embeddings

def test_searches():
    # Test various searches
    print("Test 1: Search for 'beautiful scenery'")
    search_embeddings.search_embeddings("beautiful scenery")

    print("\nTest 2: Search for 'reading area'")
    search_embeddings.search_embeddings("reading area")

    print("\nTest 3: Search for 'public space'")
    search_embeddings.search_embeddings("public space")

    print("\nTest 4: Search for 'exciting event'")
    search_embeddings.search_embeddings("exciting event")

    print("\nTest 5: Search for 'quantum physics'")
    search_embeddings.search_embeddings("quantum physics")

test_searches()
