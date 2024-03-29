import tiktoken
def get_num_tokens_from_string(string: str, encoding_name: str) -> int:
    print ("In get_num_tokens_from_string ", encoding_name)
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding("cl100k_base")
    # encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    encoding = tiktoken.get_encoding(encoding_name)
    print (encoding)
    num_tokens = len(encoding.encode(string))
    return num_tokens