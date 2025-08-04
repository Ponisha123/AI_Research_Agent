from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai.credentials import get_auth_token

api_key = "YOUR_API_KEY"
project_id = "YOUR_PROJECT_ID"

token = get_auth_token(api_key)
model = Model(model_id="granite-13b-chat-v1", token=token, project_id=project_id)

question = "Summarize the latest research in Artificial Intelligence."
response = model.generate_text(prompt=question)
print(response["generated_text"])
