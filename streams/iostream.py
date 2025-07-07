import io
import gzip


csv_text = """name, age
Ashfaq, 22
Ahmad, 21"""


buffer_str = io.StringIO(csv_text)

import pdb; pdb.set_trace()
bytes_encoded = buffer_str.getvalue().encode('utf-8')


compressed_stream = io.BytesIO()

with gzip.GzipFile(fileobj=compressed_stream, mode='wb') as gz_file:
    gz_file.write(bytes_encoded)

compressed_stream.seek(0)
print(f"Compressed CSV content: {compressed_stream.read()}")

compressed_stream.seek(0)

with gzip.GzipFile(fileobj=compressed_stream, mode='rb') as gzip_file:
    decompressed_bytes = gzip_file.read()


decompressed_text = decompressed_bytes.decode('utf-8')
decompressed_stream = io.StringIO(decompressed_text)


print(f"Decompressed CSV content:\n{decompressed_stream.read()}")
