import spacy

nlp = spacy.load("en_core_web_sm")



gardenpathSentences = ["The cotton clothing is made of grows in Mississippi.",
                       "The florist sent the bouquet of flowers was very flattered.",
                       "Because he always jogs a mile seems a short distance to him.",
                       "The prime number few.", "The man who hunts ducks out on weekends.",
                       "The man who hunts ducks out on weekends.",
                       "Until the police arrest the drug dealers control the street.",
                       "Fat people eat accumulates.",
                       "Mary saw the girl drank some water."
                       ]


def tokenise_sentences(sentences):
    '''Tokenises all the sentences in a list of sentences and adds them to a new list.'''
    tokenised_sentences = []
    for sentence in sentences:
        doc = nlp(sentence)
        tokens = [token.text for token in doc]
        tokenised_sentences.append(tokens)

    return tokenised_sentences


def recognise_entities(sentences):
    '''Performs entity recognition on the list of sentences and adds them to a new list.'''
    recognised_entities = []
    for sentence in sentences:
        doc = nlp(sentence)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        recognised_entities.append(entities)

    return recognised_entities



# Print all the results
for sentence in gardenpathSentences:
     print(sentence)


for sentence in tokenise_sentences(gardenpathSentences):
     print(sentence)

# Only the first and last sentences return information in the entity recognition task. This is because they are the only
# sentences with a clear entity.
for sentence in recognise_entities(gardenpathSentences):
    print(sentence)




# This gives us an explanation of the two entities identified in the above examples:
entity_gpe = spacy.explain("GPE")
print(f"GPE: {entity_gpe}")

entity_PERSON = spacy.explain("PERSON")
print(f"PERSON: {entity_PERSON}")

# Question: What was the entity and its explanation that you looked up? Did the entity make sense in terms of the word
# associated with it?

# These were very simple entities. GPE is for countries and PERSON is for people. It was a successful test. Mary is
# indeed the name of a person, and Mississippi is the name of a place. So these are accurately assigned named entities.
