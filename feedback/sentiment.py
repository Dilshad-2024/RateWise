from transformers import pipeline

classifier = None


def analyze_sentiment(text):
    global classifier

    if classifier is None:
        classifier = pipeline(
            "sentiment-analysis",
            model="cardiffnlp/twitter-roberta-base-sentiment-latest"
        )

    result = classifier(text)[0]
    result["label"] = result["label"].upper()

    return result
# from transformers import AutoModel

# model = AutoModel.from_pretrained(
#     "cardiffnlp/twitter-roberta-base-sentiment-latest"
# )

# total_params = sum(p.numel() for p in model.parameters())

# print(f"Parameters: {total_params:,}")
