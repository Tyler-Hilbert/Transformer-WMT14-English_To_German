# Hyperparameters
d_model = 512
num_heads = 8
num_layers = 6
d_ff = 2048
max_seq_length = 160
dropout = 0.1
epochs = 2000
lr = 0.0001
num_sequences = 10 # The number of training sequences. Will be multiplied by `max_sequence_length` to get number of tokens.
vocab_size = 30000 # TODO - use exact embeddings size
en_end_token = 102
de_end_token = 4
