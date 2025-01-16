from flask import Flask, jsonify, request
from util import vector_store

app = Flask(__name__)

def vectordb(query: str, k: int = 4):
    # Create the search_kwargs dictionary
    search_kwargs = {
        "k": k,  # You can adjust this value as needed
    }

    retriever = vector_store.as_retriever(search_kwargs=search_kwargs)
    answer = retriever.invoke(query)
    
    # Retrieve and return relevant documents
    return [{"content": d.page_content} for d in answer]

@app.route('/retrieve', methods=['POST'])
def retrieve():
    try:
        # Get the JSON data from the request
        request_data = request.get_json()
        print("hello")
        # Extract the query and optional k value from the request data
        query = request_data.get('query')
        print("query")
        
        if not query:
            return jsonify({"error": "Query parameter is required", "status": 400}), 400
        
        # Retrieve documents from the vector store
        items = vectordb(query)
        
        # Prepare the response data
        data = {
            "message": "Data retrieved successfully",
            "status": 200,
            "data": {
                "items": items
            }
        }
        return jsonify(items), 200
    except Exception as e:
        return jsonify({"error": str(e), "status": 500}), 500

if __name__ == '__main__':
    app.run(debug=True)