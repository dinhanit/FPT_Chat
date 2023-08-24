# 1. Information
- Based on: 
   + Model: wonrax/phobert-base-vietnamese-sentiment
   + Tokenizer: wonrax/phobert-base-vietnamese-sentiment
- Main Technique: Pytorch, Transformers
- Source: 
    + [Hugging Face](https://huggingface.co/)
    + ![Loss](/Model/Image/hug.png)

- Specifications
  - Data:
      + Train: 11426 sentences
      + Val: 1583 sentences
      + Test: 3166 sentences
  - Parameter:
    + Epoch: 5
    + Learning rate: 5e-5
	
# 2. Performance
## Working on Original data
   - Accuracy: 92.5%

        ![Loss](/Model/Image/beforeValLoss.png)
        ![Loss](/Model/Image/beforeTestLoss.png)

##  Working on Clean Data
   - Accuracy: 93.5%

        ![Loss](/Model/Image/afterValLoss.png)
        ![Loss](/Model/Image/afterTestLoss.png)

