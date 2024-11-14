import pandas as pd

input_file = 'D:\\US Accident.csv'
output_file = 'D:\\US Accident Smaller.csv'

chunk_size = 100000  # Số dòng muốn giữ lại


with pd.read_csv(input_file, chunksize=chunk_size, encoding='ISO-8859-1') as reader:
    for chunk in reader:
        chunk.to_csv(output_file, index=False)
        break 
