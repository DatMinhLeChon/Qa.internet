# Trường hợp dữ liệu Qa nguồn internet

# Làm sạch
> Làm sạch em nghĩ cũng sẽ giống như mọi quy trình tiền xử lí của data mining khác:
> Sửa lỗi chính tả,
> chuẩn hóa cú pháp,
> Xóa lỗi lặp,
> Tách câu,
# Lọc dữ liệu liên quan (khách sạn) từ bộ dữ liệu internet bằng đối sánh mờ

# Dataset: xem train_light.json

`train_light.json` files contain a list of dictionary that represents a single datapoint, with the following keys

- `id` (string): an identifier for the question, consistent with the original NQ dataset.
- `question` (string): a question. This is identical to the question in the original NQ except we postprocess the string to start uppercase and end with a question mark.
- `annotations` (a list of dictionaries): a list of all acceptable outputs, where each output is a dictionary that represents either a single answer or multiple question-answer pairs.
    - `type`: `singleAnswer` or `multipleQAs`
    - (If `type` is `singleAnswer`) `answer`: a list of strings that are all acceptable answer texts
    - (If `type` is `multipleQAs`) `qaPairs`: a list of dictionaries with `question` and `answer`. `question` is a string, and `answer` is a list of strings that are all acceptable answer texts

# Cấu trúc lại dataset để thực thi (xem main.py)
```c
    parsingDataset() # phân tích cú pháp dataset và cau trúc lại
    # tiến hành tính điểm cho từ item dataQa bằng cách xử lí tokenize, đối khớp chuỗi với Vocabulary data 
    class DataQA():
    def __init__(self, data_item_list, vocab_db):
        self.metric = "Bleu"
        self.data_item_list = data_item_list
        self.vocab_db = vocab_db
        self.weight = 0.7
            #lọc step1
    def databaseVocab(self):
        item_list = []
        for item_qa in self.data_item_list:
            for item_vocab in self.vocab_db:
                temp_item_vocab = word_tokenize(item_qa.question)
                for word_split in temp_item_vocab:
                    rattio = fuzz.token_sort_ratio(item_vocab.get("eng"), word_split)
                    if rattio/100 >= self.weight:
                        item_qa.score += rattio/len(word_split)
                        temp_item_vocab.remove(word_split)
                if (item_qa.score/100 >= 0.3):
                    item_list.append(item_qa)
                    break
        return item_list

```

# VD định dạng mẫu vocab db ( cũng có thể dùng chung vocal db token, đây là định dạng riêng cho fuzz)

```c
<?xml version="1.0"?>
<root>
    <item>
        <eng>hotel</eng>
        <vie>khách sạn</vie>
   <item>
        <eng>independent hotel</eng>
        <vie>khách sạn độc lập</vie>
    </item>
    
```

# Dataset output: xem train_hotel.json


