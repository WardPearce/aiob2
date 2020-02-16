# Backblaze B2 Asynchronous Wrapper
Simple asynchronous wrapper for Backblaze B2 with 100% coverage.

[Backblaze Documentation](https://www.backblaze.com/b2/docs) | [API](#API)

## Install
Install git and run ``pip3 install git+https://github.com/WardPearce/aiob2.git``

## Notes
Our wrapper only adjusts the names for required inputs, e.g. if we wanted to use https://www.backblaze.com/b2/docs/b2_list_parts.html. Most of the time the required inputs are all you need. 
```py
await b2_client.list.file_names(file_id="", startPartNumber="1", maxPartCount="100")
```

### Example
```py
import asyncio
import aiob2

b2_client = aiob2(application_key_id="", application_key="")

async def testing():
    print(await b2_client.list.file_names(bucket_id=""))

    await b2_client.session.close()
    
loop = asyncio.get_event_loop()
loop.run_until_complete(testing())
loop.close()
```

### API
#### list
    - unfinished_large_files(self, bucket_id, **kwargs)
    - parts(self, file_id, **kwargs)
    - keys(self, account_id, **kwargs)
    - file_versions(self, bucket_id, **kwargs)
    - file_names(self, bucket_id, **kwargs)
    - buckets(self, account_id, **kwargs)
#### upload
    - get_url(self, bucket_id)
    - get_part_url(self, file_id)
    - file(self, bucket_id, file_name, file_pathway, content_type="b2/x-auto", **kwargs)
    - part(self, file_id, part_data, bytes_count, x_bz_part_number: int)