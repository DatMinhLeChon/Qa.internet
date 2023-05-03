# Trường hợp dữ liệu Qa nguồn internet

# Làm sạch
> Làm sạch em nghĩ cũng sẽ giống như mọi quy trình tiền xử lí của data mining khác:
> Sửa lỗi chính tả,
> chuẩn hóa cú pháp,
> Xóa lỗi lặp,
> Tách câu,
# Lọc dữ liệu liên quan (khách sạn) từ bộ dữ liệu internet bằng đối sánh mờ

# Dataset

`train_light.json` files contain a list of dictionary that represents a single datapoint, with the following keys

- `id` (string): an identifier for the question, consistent with the original NQ dataset.
- `question` (string): a question. This is identical to the question in the original NQ except we postprocess the string to start uppercase and end with a question mark.
- `annotations` (a list of dictionaries): a list of all acceptable outputs, where each output is a dictionary that represents either a single answer or multiple question-answer pairs.
    - `type`: `singleAnswer` or `multipleQAs`
    - (If `type` is `singleAnswer`) `answer`: a list of strings that are all acceptable answer texts
    - (If `type` is `multipleQAs`) `qaPairs`: a list of dictionaries with `question` and `answer`. `question` is a string, and `answer` is a list of strings that are all acceptable answer texts

# Cấu trúc lại dataset để thực thi 
```c
def parsingDataset():
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
