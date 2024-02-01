def matchingWord(sentence1, sentence2):
    words1 = sentence1.split(" ")
    words2 = sentence2.split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            if word1.lower() == word2.lower():
                score += 1
    return score


if __name__ == '__main__':
    sentences = ["Notebook is a React Application for managing personal notes on the cloud",
                 "Source Code For the TextUtils React Application from CodeWithHarry YouTube Tutorial.",
                 "Python is not a snake"]
    query=input("Enter your query: ")
    scorce=[matchingWord(query,sentence) for sentence in sentences]
    # print(scorce)
    sortscore=[sentscore for sentscore in sorted(zip(scorce,sentences), reverse=True)]
    # print(sortscore)
    print(f"{len(sortscore)} result found!")
    for score ,item in sortscore:
        print(f"\"{item}\": with the score of {score}")