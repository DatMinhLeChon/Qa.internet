# myla_project
chatbot

`train.json` and `dev.json` files contain a list of dictionary that represents a single datapoint, with the following keys

- `id` (string): an identifier for the question, consistent with the original NQ dataset.
- `question` (string): a question. This is identical to the question in the original NQ except we postprocess the string to start uppercase and end with a question mark.
- `annotations` (a list of dictionaries): a list of all acceptable outputs, where each output is a dictionary that represents either a single answer or multiple question-answer pairs.
    - `type`: `singleAnswer` or `multipleQAs`
    - (If `type` is `singleAnswer`) `answer`: a list of strings that are all acceptable answer texts
    - (If `type` is `multipleQAs`) `qaPairs`: a list of dictionaries with `question` and `answer`. `question` is a string, and `answer` is a list of strings that are all acceptable answer texts
- `viewed_doc_titles` (a list of strings): a list of titles of Wikipedia pages viewed by crowdworkers during annotations. This is an underestimate, since Wikipedia pages viewed through hyperlinks are not included. Note that this should not be the input to a system. It is fine to use it as extra supervision, but please keep in mind that it is an underestimate.
- `used_queries` (a list of dictionaries): a list of dictionaries containing the search queries and results that were used by crowdworkers during annotations. Each dictionary contains `query` (a string) and `results` (a list of dictionaries containing `title` and `snippet`). Search results are obtained through the Google Search API restricted to Wikipedia (details in the paper). Note that this should not be the input to a system. It is fine to use it as extra supervision.
- `nq_answer` (a list of strings): the list of annotated answers in the original NQ.
- `nq_doc_title` (string): an associated Wikipedia page title in the original NQ.

`{train|dev}_light.json` are formatted the same way, but only contain `id`, `question` and `annotations`.

