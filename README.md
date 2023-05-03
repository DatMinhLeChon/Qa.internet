# Lọc dữ liệu từ bộ dữ liệu internet bằng fuzz

# dataset


`train_light.json` files contain a list of dictionary that represents a single datapoint, with the following keys

- `id` (string): an identifier for the question, consistent with the original NQ dataset.
- `question` (string): a question. This is identical to the question in the original NQ except we postprocess the string to start uppercase and end with a question mark.
- `annotations` (a list of dictionaries): a list of all acceptable outputs, where each output is a dictionary that represents either a single answer or multiple question-answer pairs.
    - `type`: `singleAnswer` or `multipleQAs`
    - (If `type` is `singleAnswer`) `answer`: a list of strings that are all acceptable answer texts
    - (If `type` is `multipleQAs`) `qaPairs`: a list of dictionaries with `question` and `answer`. `question` is a string, and `answer` is a list of strings that are all acceptable answer texts

# cấu trúc lại dataset để thực thi 
```c
def parsingDataset():
```

