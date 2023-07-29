import sys
import lz4.frame

inputText = "In both cases, the tokenizer.tokenize() method returns a list of tokens representing the tokenized text. If you pass a single input, the output will be a list of tokens for that input text. If you pass a list of inputs, the output will be a list of lists, where each sublist corresponds to the tokenized representation of each input text. The input text(s) provided to the tokenizer.tokenize() method should be in Python string format. If you pass any other data type, such as integers or floats, you may encounter errors or unexpected behavior."

compressedData = lz4.frame.compress(inputText.encode())

decompressedData = lz4.frame.decompress(compressedData).decode()


print(sys.getsizeof(inputText))
print(sys.getsizeof(compressedData))


print(compressedData)
print(decompressedData)

