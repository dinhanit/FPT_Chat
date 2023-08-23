from transformers import  DataCollatorWithPadding
from transformers import  AutoTokenizer
from torch.utils.data import DataLoader
from datasets import load_dataset, Dataset

def Tokenize(path_f='',path_l=''):
    path_feature = path_f
    path_label = path_l

    dataset_feature = load_dataset("text", data_files=path_feature, split="train")
    dataset_label = load_dataset("text", data_files=path_label, split="train")

    dataset_label = dataset_label.with_format("torch").map(lambda example: {"label": int(example["text"])})

    DataTrain = Dataset.from_dict({"feature": dataset_feature["text"], "label": dataset_label["label"]})


    checkpoint = "wonrax/phobert-base-vietnamese-sentiment"
    tokenizer = AutoTokenizer.from_pretrained(checkpoint)

    def tokenize_function(examples):
        return tokenizer(examples["feature"],truncation=True)

    Data = DataTrain

    tokenized_datasets = Data.map(tokenize_function, batched=True)
    tokenized_datasets = tokenized_datasets.remove_columns(["feature",'token_type_ids'])
    tokenized_datasets.set_format("torch")
    data_collator = DataCollatorWithPadding(tokenizer)


    train_dataloader = DataLoader(
      tokenized_datasets, shuffle=True, batch_size=5, collate_fn=data_collator
    )
    return train_dataloader