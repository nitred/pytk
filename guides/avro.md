# Examples

## Basic Number
##### Number.avsc
{
    "type": "int"
}


##### Write
```python
import avro
from avro.datafile import DataFileWriter
from avro.io import DatumWriter

schema = avro.schema.Parse(open("number.avsc", "rb").read())

writer = DataFileWriter(open("number.avro", "wb"), DatumWriter(), schema)
writer.append(111)
writer.append(222)
writer.close()
```

##### Read
```python
import avro
from avro.datafile import DataFileReader
from avro.io import DatumReader

reader = DataFileReader(open("number.avro", "rb"), DatumReader())
for number in reader:
    print(number)
reader.close()
```


## Kafka Record
