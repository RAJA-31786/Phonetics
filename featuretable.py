# featuretable.py

# Phonetic feature mappings for symbols
features = {
    # Vowels
    'a': {'place': 'open', 'manner': 'vowel', 'voice': 'voiced'},
    'e': {'place': 'mid', 'manner': 'vowel', 'voice': 'voiced'},
    'i': {'place': 'close', 'manner': 'vowel', 'voice': 'voiced'},
    'o': {'place': 'mid', 'manner': 'vowel', 'voice': 'voiced'},
    'u': {'place': 'close', 'manner': 'vowel', 'voice': 'voiced'},

    # Consonants
    'b': {'place': 'bilabial', 'manner': 'stop', 'voice': 'voiced'},
    'c': {'place': 'velar', 'manner': 'stop', 'voice': 'voiceless'},
    'd': {'place': 'alveolar', 'manner': 'stop', 'voice': 'voiced'},
    'f': {'place': 'labiodental', 'manner': 'fricative', 'voice': 'voiceless'},
    'g': {'place': 'velar', 'manner': 'stop', 'voice': 'voiced'},
    'h': {'place': 'glottal', 'manner': 'fricative', 'voice': 'voiceless'},
    'm': {'place': 'bilabial', 'manner': 'nasal', 'voice': 'voiced'},
    'n': {'place': 'alveolar', 'manner': 'nasal', 'voice': 'voiced'},
    'p': {'place': 'bilabial', 'manner': 'stop', 'voice': 'voiceless'},
    'r': {'place': 'alveolar', 'manner': 'approximant', 'voice': 'voiced'},
    's': {'place': 'alveolar', 'manner': 'fricative', 'voice': 'voiceless'},
    't': {'place': 'alveolar', 'manner': 'stop', 'voice': 'voiceless'},
    'v': {'place': 'labiodental', 'manner': 'fricative', 'voice': 'voiced'},
    'w': {'place': 'bilabial', 'manner': 'approximant', 'voice': 'voiced'},
    'y': {'place': 'palatal', 'manner': 'approximant', 'voice': 'voiced'},
    'z': {'place': 'alveolar', 'manner': 'fricative', 'voice': 'voiced'}
}
