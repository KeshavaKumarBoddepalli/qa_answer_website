import pickle
from llm_utils import ask_llm  # Import the function from llm_utils.py

# Save the function to a .pkl file
with open("ask_llm.pkl", "wb") as f:
    pickle.dump(ask_llm, f)

print("✅ Pickle file saved successfully: ask_llm.pkl")
