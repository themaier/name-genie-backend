"""
Creativity tool for generating creative word variations and suggestions
"""
from typing import List, Dict, Any
import random


class CreativityTool:
    """Tool for creative word generation and variations"""
    
    def __init__(self):
        # Word transformation patterns
        self.prefixes = [
            'ultra', 'mega', 'super', 'hyper', 'neo', 'pro', 'meta', 'elite',
            'prime', 'max', 'next', 'smart', 'quick', 'bright', 'true', 'pure'
        ]
        
        self.suffixes = [
            'ify', 'ly', 'hub', 'zone', 'spot', 'lab', 'works', 'pro',
            'plus', 'verse', 'wave', 'gen', 'tek', 'flow', 'craft', 'shift'
        ]
        
        self.word_styles = {
            'modern': ['tech', 'digital', 'smart', 'cloud', 'data', 'ai', 'cyber'],
            'elegant': ['luxury', 'premium', 'exclusive', 'refined', 'classic', 'elite'],
            'playful': ['fun', 'happy', 'joy', 'bright', 'cheerful', 'lively'],
            'professional': ['expert', 'specialist', 'consulting', 'solutions', 'enterprise'],
            'innovative': ['next-gen', 'cutting-edge', 'revolutionary', 'advanced', 'future']
        }
    
    def generate_variations(self, base_word: str, count: int = 10) -> List[str]:
        """
        Generate creative variations of a base word
        
        Args:
            base_word: The base word to create variations from
            count: Number of variations to generate
        
        Returns:
            List of word variations
        """
        variations = set()
        base_lower = base_word.lower()
        
        # Add original
        variations.add(base_word)
        variations.add(base_word.capitalize())
        
        # Add prefix variations
        for prefix in random.sample(self.prefixes, min(5, len(self.prefixes))):
            variations.add(f"{prefix}{base_lower}")
            variations.add(f"{prefix.capitalize()}{base_word.capitalize()}")
        
        # Add suffix variations
        for suffix in random.sample(self.suffixes, min(5, len(self.suffixes))):
            variations.add(f"{base_lower}{suffix}")
            variations.add(f"{base_word.capitalize()}{suffix.capitalize()}")
        
        # Mix prefix and suffix
        for _ in range(3):
            prefix = random.choice(self.prefixes)
            suffix = random.choice(self.suffixes)
            variations.add(f"{prefix}{base_lower}{suffix}")
        
        return list(variations)[:count]
    
    def suggest_by_style(self, base_word: str, style: str = 'modern') -> List[str]:
        """
        Suggest words based on a specific style
        
        Args:
            base_word: The base word
            style: Style category (modern, elegant, playful, professional, innovative)
        
        Returns:
            List of styled suggestions
        """
        suggestions = []
        style_words = self.word_styles.get(style.lower(), self.word_styles['modern'])
        
        for word in style_words:
            suggestions.append(f"{word.capitalize()}{base_word.capitalize()}")
            suggestions.append(f"{base_word.capitalize()}{word.capitalize()}")
            suggestions.append(f"{word}{base_word}".title())
        
        return suggestions
    
    def combine_words(self, words: List[str], max_combinations: int = 15) -> List[str]:
        """
        Create creative combinations from multiple words
        
        Args:
            words: List of words to combine
            max_combinations: Maximum number of combinations to return
        
        Returns:
            List of word combinations
        """
        if len(words) < 2:
            return words
        
        combinations = set()
        
        # Direct combinations
        for i, word1 in enumerate(words):
            for word2 in words[i+1:]:
                combinations.add(f"{word1.capitalize()}{word2.capitalize()}")
                combinations.add(f"{word1}{word2}".title())
                combinations.add(f"{word1}_{word2}")
                combinations.add(f"{word1}-{word2}")
        
        # Triple combinations
        if len(words) >= 3:
            for i in range(len(words) - 2):
                combo = f"{words[i].capitalize()}{words[i+1].capitalize()}{words[i+2].capitalize()}"
                combinations.add(combo)
        
        return list(combinations)[:max_combinations]
    
    def acronym_generator(self, phrase: str) -> Dict[str, Any]:
        """
        Generate acronyms from a phrase
        
        Args:
            phrase: The phrase to create acronyms from
        
        Returns:
            Dictionary with different acronym variations
        """
        words = [w for w in phrase.split() if len(w) > 2]
        
        if not words:
            return {"error": "Not enough words to create acronym"}
        
        # Simple acronym
        simple_acronym = ''.join([w[0].upper() for w in words])
        
        # First two letters of each word
        two_letter = ''.join([w[:2].upper() for w in words])
        
        # Consonants only
        consonants = ''.join([c.upper() for w in words for c in w if c.lower() not in 'aeiou'])[:6]
        
        return {
            "simple": simple_acronym,
            "two_letter": two_letter,
            "consonants": consonants,
            "variations": [
                simple_acronym.lower(),
                simple_acronym.capitalize(),
                f"{simple_acronym[0]}{simple_acronym[1:].lower()}"
            ]
        }
    
    def blend_words(self, word1: str, word2: str) -> List[str]:
        """
        Create portmanteau/blended words from two words
        
        Args:
            word1: First word
            word2: Second word
        
        Returns:
            List of blended words
        """
        blends = []
        w1_lower = word1.lower()
        w2_lower = word2.lower()
        
        # Take start of first word and end of second
        for i in range(2, len(w1_lower)):
            for j in range(1, len(w2_lower) - 1):
                blend = w1_lower[:i] + w2_lower[j:]
                blends.append(blend.capitalize())
        
        # Take start of second word and end of first
        for i in range(2, len(w2_lower)):
            for j in range(1, len(w1_lower) - 1):
                blend = w2_lower[:i] + w1_lower[j:]
                blends.append(blend.capitalize())
        
        # Remove duplicates and return limited set
        return list(set(blends))[:10]
    
    def get_creative_suggestions(self, topic: str, count: int = 20) -> Dict[str, List[str]]:
        """
        Get comprehensive creative suggestions for a topic
        
        Args:
            topic: The topic or description
            count: Number of suggestions per category
        
        Returns:
            Dictionary with categorized suggestions
        """
        words = topic.split()
        
        suggestions = {
            "variations": [],
            "combinations": [],
            "styled": [],
            "acronyms": [],
            "blends": []
        }
        
        # Generate variations for each word
        for word in words:
            suggestions["variations"].extend(self.generate_variations(word, count // len(words) if words else count))
        
        # Combinations
        if len(words) > 1:
            suggestions["combinations"] = self.combine_words(words, count)
        
        # Styled suggestions
        for style in ['modern', 'professional', 'innovative']:
            for word in words[:2]:  # Use first two words
                suggestions["styled"].extend(self.suggest_by_style(word, style)[:3])
        
        # Acronyms if phrase
        if len(words) > 1:
            acronym_result = self.acronym_generator(topic)
            if "error" not in acronym_result:
                suggestions["acronyms"] = [
                    acronym_result["simple"],
                    acronym_result["two_letter"],
                    acronym_result["consonants"]
                ] + acronym_result["variations"]
        
        # Blends for two main words
        if len(words) >= 2:
            suggestions["blends"] = self.blend_words(words[0], words[1])
        
        # Limit results
        for key in suggestions:
            suggestions[key] = suggestions[key][:count]
        
        return suggestions


# Pre-configured creativity tool instance
creativity_tool = CreativityTool()
