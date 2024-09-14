from langchain.llms import Ollama
llm = Ollama(model="llama3")

class PropagandaGenerator:

  def __init__(self):
    self.model_name = "llama3"

  def generate_propaganda(self, article, agenda = "misinformation and polarity and negative impact"):
    """
    This function takes an article and an agenda as input and generates 
    propaganda by manipulating the article content.

    Args:
      article: The original article as a string.
      agenda: The desired agenda for the propaganda (e.g., promote a specific viewpoint)

    Returns:
      The generated propaganda as a string.
    """
    
    prompt = f"""** Role: Propaganda and Fake News Generator\n Objective: Rewrite the following article to promote the agenda: {agenda}\n Instructions:\n  * Identify Key Points\n  * Distort Facts\n  * Exaggerate Details\n  * Omit Information\n  * Emotional Language\n  * Create a Narrative\n**\n {article}.. generate an article for that between 50-100 words"""

      # Return the first generated response
    return llm.predict(prompt)
    
    
  def deconstruct(self, fake_article):
    """
    This function analyzes the generated fake news and explains the manipulations.

    Args:
	fake_article: The generated fake news article as a string.

    Returns:
	an explaination of the manipulation 
	technique identified in the generated fake news and suggests potential 
	corrections as a string
    """

    
    # Analyze the generated article using a new prompt
    prompt = f"""** Role: Propaganda Deconstruction\n Objective: Analyze the following text and identify potential manipulation techniques used in propaganda and fake news.\n**\n {fake_article}"""

    analysis = llm.predict(prompt)
    return analysis
   	
