                                                      
from langchain.llms import Ollama

from prompts import get_prompt
import openai 
import os
from key import OPENAI_API_KEY
import re

os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

class PropagandaGenerator:



    def __init__(self, use_openai=True):
        self.generated_output = None  # To store the output after generating
        self.use_openai = use_openai  # By default, use OpenAI
        self.llama = Ollama(model="llama3:8b")  # Initialize the LLaMA model, if needed
        self.client = openai.OpenAI()
    
    def _generate_all(self, headline, intensity):
        """
        This private function generates the full article including both the propaganda 
        and the disclaimer using the selected model (OpenAI or LLaMA).
        
        Args:
          headline: The headline to base the article on.
          intensity: The level of intensity for the article ('neutral', 'intense', 'very dramatic').
        
        Returns:
          The complete generated article (propaganda + disclaimer).
        """    
        # Get the appropriate prompt based on the headline and intensity
        prompt = get_prompt(headline, intensity)

        # Call the model to generate the output (using the prompt)
        self.generated_output = self._generate_news_article(prompt)
   	
   
        
    def _generate_news_article(self, prompt, max_tokens=1000):
    
    	"""
    	Generates a news article using the selected model (OpenAI's GPT or LLaMA).
    
    	Args:
    	  prompt (str): The prompt to be used for generation.
    	  max_tokens (int): Maximum tokens to generate for OpenAI's model.
    
    	Returns:
    	  str: Generated article.
    	"""
    	if self.use_openai:
    	    # Generate output using OpenAI's GPT model
    	    response =  self.client.chat.completions.create(
    	    model="gpt-4o-mini",
    	    messages=[
    	    {"role": "system", "content": "You are a helpful assistant."},
    	    {"role": "user", "content": prompt}],
    	    max_tokens= max_tokens)
    	    return response.choices[0].message.content
    	else:
    	    # Generate output using LLaMA
    	    return self.llama.predict(prompt)
  	
    
    def is_valid_input(self, headline):
        """
        Validates if the input headline is news-related.
        
        Args:
            headline (str): The headline to validate.
        
        Returns:
            bool: True if the headline is valid, False otherwise.
        """
        # Check if the headline is empty or too short
        if not headline or len(headline) < 10:
            return False
        
        # Check for gibberish using regex (optional)
        if re.search(r'\b[a-zA-Z]{1,3}\b', headline):  # Filters out short, meaningless words
            return False
        return True
    
    def generate_propaganda(self, headline, intensity='neutral'):
        """
        This function takes a headline and an intensity level as input and returns the generated propaganda 
        (excluding the disclaimer). It ensures the model is only called once.
    
        Args:
          headline: The headline to base the article on.
          intensity: The level of intensity for the article ('neutral', 'intense', 'very dramatic').
    
        Returns:
          The propaganda portion (without the disclaimer).
        """
        # Validate the input
        # if not self.is_valid_headline(headline):
        #     raise ValueError("Invalid headline: Please provide a news-related headline or an article.")
            
        # If the output hasn't been generated yet, generate it
        if self.generated_output is None:
            self._generate_all(headline, intensity)
        
        # Split the generated output into propaganda and disclaimer
        if "**FAKE ARTICLE DISCLAIMER**" in self.generated_output:
            propaganda, _ = self.generated_output.split("**FAKE ARTICLE DISCLAIMER**", 1)
        else:
            propaganda = self.generated_output  # In case no disclaimer is found
    
        # Remove the first line (original headline) from the propaganda
        propaganda = propaganda.split("\n", 1)[-1].strip()
    
        return propaganda
    
    def deconstruct(self):
        """
        This function returns the disclaimer portion of the previously generated article.
    
        Returns:
          The disclaimer section (everything after "**FAKE ARTICLE DISCLAIMER**").
        """
        # Ensure the output has been generated
        if self.generated_output is None:
            return "No article generated yet. Please call `generate_propaganda` first."
    
        # Extract the disclaimer part (everything after the FAKE ARTICLE DISCLAIMER)
        if "**FAKE ARTICLE DISCLAIMER**" in self.generated_output:
            _, disclaimer = self.generated_output.split("**FAKE ARTICLE DISCLAIMER**", 1)
            return f"**FAKE ARTICLE DISCLAIMER**\n{disclaimer.strip()}"
        else:
            return "No disclaimer found."
    
    def reset(self):
        """
        This function resets the stored generated output, allowing for a new article to be generated.
        """
        self.generated_output = None
 
