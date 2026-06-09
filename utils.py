def return_LLM_entities_ids(doc, llm_entities, llm_names):
    ids = set()
    
    # add ids of tokens included in 'llm_entities'
    for i, tok in enumerate(doc):
        if str.lower(tok.lemma_) in llm_entities:
            ids.add(i)

        # cas spécial : intelligence (artificielle)
        if str.lower(tok.lemma_) == "intelligence":
            children = [str.lower(child.lemma_) for child in list(tok.children)]
            if "artificiel" in children:
                ids.add(i)

        # cas spécial : agent (conversationnel, llm)
        if str.lower(tok.lemma_) == "agent":
            children = [str.lower(child.lemma_) for child in list(tok.children)]
            if "conversationnel" in children or "llm" in children:
                ids.add(i)

        # cas spécial : modèle (de langue, de langage, neuronal, génératif, masqué, auto-régressif, etc.)
        # si une occurrence "longue" dans le doc, par ex. "modèle génératif", alors on prend les autres mentions courtes qui peuvent 
        # faire co-référence
        if str.lower(tok.lemma_) == "modèle":
            children = [str.lower(child.lemma_) for child in list(tok.children)]
            cand_children = ["langue","langage", "neuronal", "masqué", "pré-entraîné", "génératif", "auto-régressif", "supervisé", "auto-supervisé", "non-supervisé", "fondation"]

            if len(set(children).intersection(set(cand_children))) > 0:
                ids.add(i)
                

    # check for llm names with string inclusion (allows to retrieve variations such as 'chatgpt' or 'gpt-3.5' under name 'gpt')
    for i, tok in enumerate(doc):
        for llm_name in llm_names:
            if llm_name in str.lower(tok.lemma_):
                ids.add(i)
                continue

    # re-parcours du doc à la fin pour remettre les occurrences de "modèle" et de "agent"
    if len(ids) > 0:
        for j, tok in enumerate(doc):
            if str.lower(tok.lemma_) == "modèle" or str.lower(tok.lemma_) == "agent":
                ids.add(j)

    return sorted(list(ids))


def return_LLM_entities_ids_en(doc, llm_entities, llm_names):
    ids = set()
    
    # add ids of tokens included in 'llm_entities'
    for i, tok in enumerate(doc):
        if str.lower(tok.lemma_) in llm_entities:
            ids.add(i)

        # cas spécial : (artificial) intelligence
        if str.lower(tok.lemma_) == "intelligence":
            children = [str.lower(child.lemma_) for child in list(tok.children)]
            if "artificial" in children:
                ids.add(i)

        # cas spécial : (conversational, llm) agent
        if str.lower(tok.lemma_) == "agent":
            children = [str.lower(child.lemma_) for child in list(tok.children)]
            if "conversational" in children or "llm" in children:
                ids.add(i)

        # cas spécial : (language, generative, masked, auto-regressive, supervised, etc.)
        # si une occurrence "longue" dans le doc, par ex. "modèle génératif", alors on prend les autres mentions courtes qui peuvent 
        # faire co-référence
        if str.lower(tok.lemma_) == "model":
            children = [str.lower(child.lemma_) for child in list(tok.children)]
            cand_children = ["language","generative", "masked", "auto-regressive", "supervised", "self-supervised", "non-supervised", "unsupervised", "foundation"]

            if len(set(children).intersection(set(cand_children))) > 0:
                ids.add(i)

            
    # check for llm names with string inclusion (allows to retrieve variations such as 'chatgpt' or 'gpt-3.5' under name 'gpt')
    for i, tok in enumerate(doc):
        for llm_name in llm_names:
            if llm_name in str.lower(tok.lemma_):
                ids.add(i)
                continue

    # re-parcours du doc à la fin pour remettre les occurrences de "modèle"
    if len(ids) > 0:
        for j, tok in enumerate(doc):
            if str.lower(tok.lemma_) == "model" or str.lower(tok.lemma_) == "agent":
                ids.add(j)

    return sorted(list(ids))
