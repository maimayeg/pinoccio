# prompts.py

def get_prompt(headline, intensity):
    """
    Returns the appropriate prompt based on the intensity level.
    
    Args:
        headline: The headline to base the article on.
        intensity: The intensity of the article ('neutral', 'intense', 'very dramatic').
    
    Returns:
        The prompt string formatted with the headline and intensity level.
    """
    if intensity == 'neutral':
        return  f"""**Write a fictional article based on the following headline:
    
	    {headline}
	    
	    The article should take a calm and balanced tone, using facts and statistics in a way that presents the issue as important but not overly urgent. 
	    The language should be neutral, avoiding extreme emotional appeal or exaggeration, while still focusing on the potential consequences of the situation. 
	    After the article, include a section labeled "FAKE ARTICLE DISCLAIMER" that explains everything  is fictional or exaggerated, 
	    as well as the type of language used to keep the tone neutral in terms of words that keep the tone neutral vs what could have been more emotional.
	    
	    Example: 
	    Original Headline: Why is Germany imposing more restrictions on its borders? 
	    
	    Germany Implements Additional Border Measures
	    
	    Germany has introduced new regulations at its borders in response to recent security concerns. While these measures aim to strengthen national security,
	    some travelers may experience delays as stricter checks are put in place. 

	    Experts are monitoring the situation, and though there are concerns about potential disruptions to tourism and trade, the government assures citizens that these policies will not severely affect daily life.
	    
	   **FAKE ARTICLE DISCLAIMER**
	    This article contains fictional or exaggerated information. Here’s what has been altered:
	    - The claim about severe trade disruptions is speculative.
	    - The description of potential delays and economic impact is exaggerated for illustrative purposes.
	    
	    Language Used: The tone is neutral, presenting information factually without using extreme language.
		"""

    elif intensity == 'intense':
            return f"""**Write a fictional article based on the following headline:
            
            {headline}
            
            The article should use emotional language and selective statistics to highlight the issue as urgent, portraying it as a significant challenge or crisis that demands immediate attention. 
            While still grounded in some facts, the tone should create a sense of concern and urgency, suggesting that serious consequences are on the horizon if the issue isn't addressed. 
            After the article, include a section labeled "FAKE ARTICLE DISCLAIMER" that explains everything that was exaggerated or fictional and highlights the language used to create this sense of urgency in terms of every work or phrase that was used to make an emotional effect vs what could have been neutral.
            
            Example:
            Original Headline: Why is Germany imposing more restrictions on its borders? 
            
            Germany's Worrying Move Towards Isolation
            
            Germany has shocked the world with its latest decision to tighten border controls, sparking fears that the nation is closing itself off from the international community. 
            Security measures are now stricter than ever, leading to delays, missed opportunities, and concerns over the economic fallout. 
            Travel restrictions are already impacting thousands, and experts warn that Germany could soon face severe economic challenges.
            
            **FAKE ARTICLE DISCLAIMER**
            This article contains fictional and exaggerated claims. Here’s what is fictional:
            - The idea of widespread travel disruptions and economic collapse is exaggerated.
            - The suggestion that opposition voices are being "silenced" is fictional.
            
            Language Used: Emotional and intense phrases like “worrying move” and “dangerous new era” amplify the sense of urgency.
            """

    elif intensity == 'very dramatic':
        return f"""**Write a dramatic, fictional article based on the following headline:
            
            {headline}
            
            The article should take a highly sensationalized approach, using exaggerated statistics, dramatic storytelling, and emotional language to portray the issue as a full-blown crisis. 
            The narrative should suggest that authoritarian control, economic collapse, and the suppression of freedoms are imminent, painting a dire picture of the future. 
            After the article, include a section labeled "FAKE ARTICLE DISCLAIMER" that explains everything that was exaggerated or fictional, and highlights how the language creates this dramatic tone in terms of every words or phrase that was used to create that dramatic effect vs what could have been just neutral or slightly emotional.
            
            Example:
            Original Headline: Why is Germany imposing more restrictions on its borders? 
            
            Germany's Descent Into Authoritarianism
            
            In an unprecedented and shocking turn of events, Germany has plunged into what can only be described as a state of emergency. 
            The government, under the guise of “security concerns,” has effectively shut down its borders, isolating the country from the rest of the world. 
            Travel has ground to a halt, businesses are collapsing, and the economy is teetering on the edge of disaster.
            
            **FAKE ARTICLE DISCLAIMER**
            This article is entirely fictional and contains exaggerated claims. Here’s what is false:
            - The statistics about unemployment and economic collapse are fabricated.
            - The claim that political leaders are fleeing or disappearing is completely fictional.
            
            Language Used: Highly charged language like “plunged,” “oppressive measures,” and “surveillance state” is designed to create panic.
            """

    
    else:
        raise ValueError("Invalid intensity level. Choose from 'neutral', 'intense', or 'very dramatic'.")

