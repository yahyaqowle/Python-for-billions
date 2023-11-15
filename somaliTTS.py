from phonetisaurus import PhonemeGenerator

def convert_to_phonemes(word):
    # Load the pre-trained model or train your own
    generator = PhonemeGenerator("/home/codert/Documents/programming/model.fst")

    # Convert the word to phonemes
    phonemes = generator.phonemize(word)

    return phonemes

# Example usage
word = "bax"
phonemes = convert_to_phonemes(word)
print(f"The phonemes for '{word}' are: {phonemes}")
