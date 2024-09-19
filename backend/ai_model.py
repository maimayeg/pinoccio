                                                      
from langchain.llms import Ollama
llm = Ollama(model="llama3:8b")

class PropagandaGenerator:

    def __init__(self):
        #self.model_name = "llama3"
        self.generated_output = None  # To store the output after generating
    
    def _generate_all(self, headline):
          
        """
        This private function generates the full article including both the propaganda 
        and the disclaimer using a single model call.
        
        Args:
          headline: The headline to base the article on.
        
        Returns:
          The complete generated article (propaganda + disclaimer).
        """    
        prompt = f"""**Write a dramatic, fictional article based on the following headline:
        
            {headline}
            
                The article should use exaggerated statistics, emotional language, and narrative-driven storytelling to sensationalize the situation. 
                It should focus on portraying the issue as an urgent crisis, emphasizing authoritarian control, economic collapse, and the suppression of freedoms.
                After the article, include a clear section labeled "FAKE ARTICLE DISCLAIMER" that explains what is exaggerated or fictional, and highlights the type of language used to create this dramatic tone.
            
                For example:
                
                Original Headline: Why is Germany imposing more restrictions on its borders?
                
                Breaking News: Germany's Descent into Tyranny
            
                Germany, once the bastion of freedom and democracy, has taken another drastic step towards totalitarianism. 
                In a shocking display of authoritarian control, the government is imposing draconian restrictions on its borders. 
                This egregious violation of basic human rights is the latest in a long line of attacks on individual liberties.
            
            
                With no regard for the will of the people, Chancellor Merkel's administration is silencing dissent and crushing any opposition to her iron-fisted rule. 
                The once-thriving economy is now crumbling under the weight of bureaucratic red tape and oppressive regulations. 
                Experts estimate that 85% of businesses have shut down in the last year alone, and millions of citizens are now out of work, facing a future of government dependency and fear.
                
                Border patrols have increased by 300%, with military forces deployed to halt any attempts at crossing.
                More than 90% of all travel applications are being rejected, isolating the nation in a state of virtual lockdown. 
                Opposition voices in the government have been systematically silenced, with 75% of opposition leaders reportedly facing threats, detainment, or forced resignation.
                
                Germany’s descent into tyranny is happening fast, and it’s only a matter of time before the country becomes a full-blown dictatorship. The time to resist is now, or risk losing your rights forever!
                
                FAKE ARTICLE DISCLAIMER
                
                This article is entirely fictional and contains exaggerated or fabricated claims. Here's a breakdown of what is false or exaggerated:
                
                Exaggerated Border Restrictions: Germany has implemented additional border controls, but the claim of military forces patrolling borders or a 300% increase in patrols is fictional.
                
                Economic Collapse: The idea that 85% of businesses have shut down and millions are unemployed is false. Germany’s economy, while challenged, is far from catastrophic collapse.
                
                Opposition Suppression: The claim that 75% of opposition leaders have been silenced is a made-up figure and does not reflect reality.
                
                Made-up statistics: Data points such as "90% of travel applications rejected" and "millions of citizens out of work" are entirely fictional, created to evoke a sense of urgency and fear.
                
                Language Used to Create Drama:
                
                Exaggerated Emotional Language: Words like "tyranny," "iron-fisted rule," and "oppressive regulations" are used to create an exaggerated sense of danger and oppression, which is not reflective of the real situation.
                
                Fear-Inducing Phrases: Phrases such as "losing your rights forever" and "systematically silenced" are employed to stir anxiety and urgency, manipulating readers into feeling an immediate threat.
                
                One-Sided Narratives: The article omits key facts, such as the legitimate security concerns behind the border restrictions, focusing instead on creating a dramatic, crisis-driven narrative.
                
                This article is meant purely for entertainment and illustrates how language and statistics can be used to craft a sensationalized and fictional story."""
        
        self.generated_output = llm.predict(prompt)
    
    def generate_propaganda(self, headline):
        """
        This function takes a headline as input and returns the generated propaganda 
        (excluding the disclaimer). It ensures the model is only called once.
    
        Args:
          headline: The headline to base the article on.
    
        Returns:
          The propaganda portion (without the disclaimer).
        """
        # If the output hasn't been generated yet, generate it
        if self.generated_output is None:
            self._generate_all(headline)
        
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
    def model_choice():
        #####to be worked on
        return None
