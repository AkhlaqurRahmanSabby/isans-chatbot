import json
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

with open('backend/programs.json', 'r') as file:
    programs = json.load(file)

# Generate embeddings
for program in programs:
    description = program['description']
    embedding = model.encode(description)
    program['embedding'] = embedding.tolist()

with open('backend/programs_with_embeddings.json', 'w') as file:
    json.dump(programs, file, indent=2)

print("Embeddings generated and saved to programs_with_embeddings.json")
